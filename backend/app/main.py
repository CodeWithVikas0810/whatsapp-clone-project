from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.chats import router as chats_router
from app.routers.messages import router as messages_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(chats_router)
app.include_router(messages_router)
