from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    phone_number: str
    username: str
    password: str
    display_name: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str
    display_name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class SearchUser(BaseModel):
    id: UUID
    username: str
    display_name: str
