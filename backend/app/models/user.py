import uuid
import enum

from datetime import datetime

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, default=uuid.uuid4
    )
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    display_name: Mapped[str] = mapped_column(nullable=False)
    profile_picture: Mapped[str | None] = mapped_column()
    about: Mapped[str | None] = mapped_column()
    is_online: Mapped[bool] = mapped_column(nullable=False, default=False)
    last_seen: Mapped[datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now
    )

    chat_participations: Mapped[list["ChatParticipant"]] = relationship(
        back_populates="user"
    )

    


class ChatType(enum.Enum):
    DIRECT = "direct"
    GROUP = "group"


class Chat(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4)

    chat_type: Mapped[ChatType] = mapped_column(
        Enum(ChatType, inherit_schema=True), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)

    participants: Mapped[list["ChatParticipant"]] = relationship(back_populates="chat")

    


class ChatParticipant(Base):
    __tablename__ = "chat_participants"

    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id"), primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    joined_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)

    chat: Mapped["Chat"] = relationship(back_populates="participants")

    user: Mapped["User"] = relationship(back_populates="chat_participations")
