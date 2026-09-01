from pwdlib import PasswordHash

from datetime import datetime, timedelta, timezone

from app.core.config import setting


import jwt

password_hash = PasswordHash.recommended()


def hash_password(password):
    hashed_password = password_hash.hash(password)
    return hashed_password


def verify_password(password, hashed_password):
    res = password_hash.verify(password, hashed_password)
    return res


def create_access_token(user_id, expires_delta: timedelta | None = None):
    to_encode = {"sub": str(user_id)}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt
