from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.database import get_db

from app.schemas.messages import MessageCreate, MessageResponse
from app.models.message import Message

from app.models.user import ChatParticipant
from app.core.security import decode_access_token

import dependencies
import jwt

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
        status="unread",
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

    async def connect(self, websocket, chat_id: int):
        await websocket.accept()

        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = []

        self.active_connections[chat_id].append(websocket)

        print(len(self.active_connections))

    def disconnect(self, websocket, chat_id):

        self.active_connections[chat_id].remove(websocket)

        if not self.active_connections[chat_id]:
            del self.active_connections[chat_id]

    async def broadcast(self, message, chat_id):

        for websocket in self.active_connections[chat_id]:
            await websocket.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):

    token = websocket.cookies.get("token")

    if token is None:
        await websocket.close(1008)
        return

    try:
        decode_token = decode_access_token(token)
        user_id = decode_token["sub"]

    except jwt.PyJWTError as exc:
        await websocket.close(1008)
        return 

    await manager.connect(websocket, chat_id)
    try:
        while True:

            message = await websocket.receive_text()

            await manager.broadcast(message, chat_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, chat_id)
        print(f"User disconnected from chat {chat_id}")
