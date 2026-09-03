import uuid
from app.core.database import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime


class Message(Base):
    __tablename__="messages"
    

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id"), nullable=False)
    sender_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
