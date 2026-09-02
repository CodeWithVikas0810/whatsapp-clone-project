import uuid
from pydantic import BaseModel

from datetime import datetime


class ChatResponse(BaseModel):
    id: int
    guid: uuid.UUID
    chat_type: str
    created_at: datetime
