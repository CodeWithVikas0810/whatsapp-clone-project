from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, or_

from sqlalchemy.orm import Session

from app.schemas.user import UserResponse, UserCreate, UserLogin, Token
from app.core.database import get_db


from app.core.security import hash_password, verify_password, create_access_token

from app.models.user import User

router = APIRouter()


@router.post("/auth/register", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Function to create user"""

    result = db.execute(
        select(User).where(
            or_(User.phone_number == user.phone_number, User.username == user.username)
        )
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        if existing_user.phone_number == user.phone_number:
            raise HTTPException(
                status_code=400, detail="Phone number already registered"
            )

        if existing_user.username == user.username:
            raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(
        username=user.username,
        password_hash=hash_password(user.password),
        display_name=user.display_name,
        phone_number=user.phone_number,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/auth/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Function for successful login"""

    username = db.execute(select(User).where(User.username == user.username))

    username_result = username.scalar_one_or_none()

    if username_result is None:
        raise HTTPException(status_code=401, detail="User not exists")

    pass_verification = verify_password(user.password, username_result.password_hash)
    if pass_verification is False:
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token(username_result.id)

    return {"access_token": token, "token_type": "bearer"}
