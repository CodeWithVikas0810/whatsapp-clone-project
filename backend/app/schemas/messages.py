import uuid
from pydantic import BaseModel


class MessageCreate(BaseModel):

    content: str


class MessageResponse(BaseModel):
    id: uuid.UUID
    chat_id: int
    sender_id:uuid.UUID
    content: str
