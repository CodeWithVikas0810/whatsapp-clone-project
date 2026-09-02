from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.chats import router as chats_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(chats_router)
