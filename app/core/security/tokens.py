from datetime import datetime, timedelta, timezone
from typing import Annotated, Union, cast

from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import Response
from jose import JWTError, jwt, ExpiredSignatureError

from app.core.settings import jwt_settings
from .settings import Settings


def create_token(data: dict, expire: datetime):
    data.update({"exp": expire})
    token = jwt.encode(
        data, 
        jwt_settings.JWT_SECRET_KEY, 
        algorithm=jwt_settings.ALGORITHM
    )
    return token


def set_and_create_tokens_cookies(response: Response, data: dict) -> None:
    expire_access = datetime.now(timezone.utc) + timedelta(
        seconds=5#jwt_settings.ACCESS_TOKEN_EXPIRATION_TIME
    )
    expire_refresh = datetime.now(timezone.utc) + timedelta(
        seconds=jwt_settings.REFRESH_TOKEN_EXPIRATION_TIME
    )
    access_token = create_token(data, expire_access)
    refresh_token = create_token(data, expire_refresh)
   
    response.set_cookie(key="access", value=access_token)
    response.set_cookie(key="refresh", value=refresh_token)


def get_token_from_cookie(request: Request):
    access_token = request.cookies.get('access')
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token not found",
        )
    try:
        data = jwt.decode(
            token=access_token, 
            key=jwt_settings.JWT_SECRET_KEY, 
            algorithms=jwt_settings.ALGORITHM
        )
    except ExpiredSignatureError:
        print("Истек срок действия токена")
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return data
