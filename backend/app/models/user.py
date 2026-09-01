from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

import uuid
from datetime import datetime


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
