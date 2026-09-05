import uuid
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MessageCreate(BaseModel):

    content: str
    


class MessageResponse(BaseModel):
    id: uuid.UUID
    chat_id: int
    sender_id: uuid.UUID
    content: str
    created_at: datetime
    status:str
    model_config = ConfigDict(from_attributes=True)


class DeliveredEvent(BaseModel):
    type: str
    message_id: uuid.UUID 
    
class ReadEvent(BaseModel):
    type:str
    message_id: uuid.UUID