from pydantic import BaseModel


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
    access_token:str
    token_type:str
    
