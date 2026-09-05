"""Reusable user authentication dependency"""

from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import (
    OAuth2PasswordBearer,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.database import get_db
from app.models.user import User
from typing import Annotated

from app.core.security import decode_access_token
import jwt

security = HTTPBearer()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# def get_current_user(
#     credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
#     db: Session = Depends(get_db),
# ):
#     token = credentials.credentials

#     try:
#         payload = decode_access_token(token)
#     except jwt.PyJWTError as exc:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Could not validate credentials",
#         ) from exc
#     user_id = payload["sub"]

#     user_info = db.execute(select(User).where(User.id == user_id))
#     user = user_info.scalar_one_or_none()

#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="User not found",
#         )
#     return user


def get_current_user(
    token: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        payload = decode_access_token(token)
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        ) from exc

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


def get_another_user(user_name: str, db: Session = Depends(get_db)):
    another_user = db.execute(select(User).where(User.username == user_name))

    user_result = another_user.scalar_one_or_none()

    return user_result
