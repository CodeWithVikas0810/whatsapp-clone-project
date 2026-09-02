from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import select, func


from app.schemas.chats import ChatResponse
from app.core.database import get_db

from app.models.user import User, ChatParticipant, Chat, ChatType


import dependencies

router = APIRouter(prefix="/chats", tags=["Chats"])


@router.post("/direct/{user_id}", response_model=ChatResponse)
def get_or_create_direct_chat(
    user_id: str,
    current_user=Depends(dependencies.get_current_user),
    db: Session = Depends(get_db),
):

    target_user = db.execute(select(User).where(User.id == user_id))
    target_user_result = target_user.scalar_one_or_none()

    if target_user_result is None:
        raise HTTPException(status_code=404, detail="User not found")

    if current_user.id == target_user_result.id:
        raise HTTPException(status_code=400, detail="Unable to process")

    existing_chat = db.execute(
        select(Chat)
        .join(ChatParticipant)
        .where(
            Chat.chat_type == ChatType.DIRECT,
            ChatParticipant.user_id.in_([current_user.id, target_user_result.id]),
        )
        .group_by(Chat.id)
        .having(func.count(ChatParticipant.user_id) == 2)
    )
    existing_chat_result = existing_chat.scalar_one_or_none()

    if existing_chat_result is None:
        new_chat = Chat(
            chat_type=ChatType.DIRECT,
        )

        current_user_participant = ChatParticipant(
            chat=new_chat,
            user_id=current_user.id,
        )
        target_user_participant = ChatParticipant(
            chat=new_chat,
            user_id=target_user_result.id,
        )
        db.add(new_chat)
        db.add(current_user_participant)
        db.add(target_user_participant)
        db.commit()
        db.refresh(new_chat)

        return new_chat

    return existing_chat_result


@router.get("/", response_model=list[ChatResponse])
def get_chats(
    current_user=Depends(dependencies.get_current_user), db: Session = Depends(get_db)
):
    chats = db.execute(
        select(Chat)
        .join(ChatParticipant)
        .where(ChatParticipant.user_id == current_user.id)
    )
    chats_result = chats.scalars().all()

    return chats_result


@router.get("/{chat_id}", response_model=ChatResponse)
def get_chat_by_id(
    chat_id: int,
    current_user=Depends(dependencies.get_current_user),
    db: Session = Depends(get_db),
):
    chat = db.execute(
        select(Chat)
        .join(ChatParticipant)
        .where(Chat.id == chat_id, ChatParticipant.user_id == current_user.id)
    )
    chat_result = chat.scalar_one_or_none()

    if chat_result is None:
        raise HTTPException(status_code=404, detail="Unable to find chat")

    return chat_result
