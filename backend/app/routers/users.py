from fastapi import APIRouter, Depends
from sqlalchemy import select

from sqlalchemy.orm import Session
from app.models.user import User

from app.schemas.user import SearchUser
from app.core.database import get_db


from app.schemas.user import UserResponse
import dependencies

router = APIRouter()


@router.get("/users/me", response_model=UserResponse)
def get_me(current_user=Depends(dependencies.get_current_user)):
    return current_user


@router.get("/users/search", response_model=list[SearchUser])
def find_user(
    user_name: str,
    current_user=Depends(dependencies.get_current_user),
    db: Session = Depends(get_db),
):
    result = db.execute(select(User).where(User.username.ilike(f"%{user_name}%")))

    other_user = result.scalars().all()

    return other_user
