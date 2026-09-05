from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.database import get_db

from app.schemas.messages import (
    MessageCreate,
    MessageResponse,
    DeliveredEvent,
    ReadEvent,
)
from app.models.message import Message

from app.models.user import ChatParticipant, User
from app.core.security import decode_access_token

from datetime import datetime

import dependencies
import jwt
import json

router = APIRouter(prefix="/messages", tags=["messages"])


@router.post("/{chat_id}", response_model=MessageResponse)
def create_message(
    chat_id: int,
    msg_content: MessageCreate,
    current_user=Depends(dependencies.get_current_user),
    db: Session = Depends(get_db),
):

    participant = db.execute(
        select(ChatParticipant).where(
            ChatParticipant.chat_id == chat_id,
            ChatParticipant.user_id == current_user.id,
        )
    )
    participant_result = participant.scalar_one_or_none()

    if participant_result is None:
        raise HTTPException(status_code=403, detail="Not authorized")

    msg = Message(
        chat_id=chat_id,
        sender_id=current_user.id,
        content=msg_content.content,
        status="sent",
    )

    db.add(msg)
    db.commit()
    db.refresh(msg)

    return msg


@router.get("/{chat_id}", response_model=list[MessageResponse])
def get_messages(
    chat_id: int,
    current_user=Depends(dependencies.get_current_user),
    db: Session = Depends(get_db),
):

    participant = db.execute(
        select(ChatParticipant).where(
            ChatParticipant.chat_id == chat_id,
            ChatParticipant.user_id == current_user.id,
        )
    )
    participant_result = participant.scalar_one_or_none()

    if participant_result is None:
        raise HTTPException(status_code=403, detail="Not authorized")

    messages = db.execute(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.created_at)
    )

    messages_result = messages.scalars().all()

    return messages_result


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket, chat_id: int, user_id):
        await websocket.accept()

        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = {}

        if user_id not in self.active_connections[chat_id]:
            self.active_connections[chat_id][user_id] = websocket

        print("Connected", self.active_connections)

    def disconnect(self, chat_id, user_id):

        del self.active_connections[chat_id][user_id]

        if not self.active_connections[chat_id]:
            del self.active_connections[chat_id]

    async def broadcast(self, message, chat_id):

        for websocket in self.active_connections[chat_id].values():
            await websocket.send_text(message)

        print("Disconnected", self.active_connections)


manager = ConnectionManager()


@router.websocket("/ws/{chat_id}")
async def websocket_endpoint(
    websocket: WebSocket, chat_id: int, db: Session = Depends(get_db)
):

    token = websocket.cookies.get("token")

    if token is None:
        await websocket.close(1008)
        return

    try:
        decode_token = decode_access_token(token)
        user_id = decode_token["sub"]

        participant = db.execute(
            select(ChatParticipant).where(
                ChatParticipant.chat_id == chat_id, ChatParticipant.user_id == user_id
            )
        )

        participant_result = participant.scalar_one_or_none()

        if participant_result is None:
            await websocket.close(1008)
            return

    except jwt.PyJWTError:
        await websocket.close(1008)
        return

    await manager.connect(websocket, chat_id, user_id)

    user = db.execute(select(User).where(User.id == user_id))

    user_info = user.scalar_one_or_none()

    if user_info is None:
        await websocket.close(1008)
        return

    user_info.is_online = True
    user_info.last_seen = None
    db.commit()

    try:
        while True:

            message = await websocket.receive_text()
            message = json.loads(message)
            if message["type"] == "delivered":
                delivered_event = DeliveredEvent.model_validate(message)

                message_query = db.execute(
                    select(Message).where(Message.id == delivered_event.message_id)
                )
                message_record = message_query.scalar_one_or_none()

                if message_record is None:
                    await websocket.close(1008)
                    return

                if message_record.sender_id == user_id:
                    await websocket.close(1008)
                    return

                if message_record.chat_id != chat_id:
                    await websocket.close(1008)
                    return

                message_record.status = "deliverd"
                db.commit()

                delivered_response = {
                    "type": "delivered",
                    "message_id": str(message_record.id),
                }

                sender_websocket = manager.active_connections[chat_id].get(
                    str(message_record.sender_id)
                )

                if sender_websocket:
                    await sender_websocket.send_text(json.dumps(delivered_response))

            if message["type"] == "read":
                read_event = ReadEvent.model_validate(message)

                message_query = db.execute(
                    select(Message).where(Message.id == read_event.message_id)
                )
                message_record = message_query.scalar_one_or_none()

                if message_record is None:
                    await websocket.close(1008)
                    return

                if message_record.chat_id != chat_id:
                    await websocket.close(1008)
                    return

                if message_record.sender_id == user_id:
                    await websocket.close(1008)
                    return

                message_record.status = "read"
                db.commit()

            if message["type"] == "message":
                msg = Message(
                    chat_id=chat_id,
                    sender_id=user_id,
                    content=message["content"],
                    status="sent",
                )
                db.add(msg)
                db.commit()
                db.refresh(msg)

                response = MessageResponse.model_validate(msg)

                await manager.broadcast(response.model_dump_json(), chat_id)

    except WebSocketDisconnect:
        manager.disconnect(chat_id, user_id)
        print(f"User disconnected from chat {chat_id}")

        user = db.execute(select(User).where(User.id == user_id))
        user_info = user.scalar_one_or_none()

        if user_info is None:
            await websocket.close(1008)
            return

        user_info.is_online = False
        user_info.last_seen = datetime.now()
