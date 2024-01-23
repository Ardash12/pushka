from typing import Union, cast

from fastapi import Depends
from fastapi.responses import Response
from fastapi_jwt_auth import AuthJWT

from app.core.settings import jwt_settings
from .settings import Settings


def set_and_create_tokens_cookies(
    response: Response, 
    subject: Union[int, str], 
    authorize: AuthJWT = Depends(),
) -> None:
    
    @AuthJWT.load_config
    def get_config():
        return Settings()

    access_token = authorize.create_access_token(
        subject=subject, 
        algorithm=jwt_settings.ALGORITHM,
        expires_time=jwt_settings.ACCESS_TOKEN_EXPIRATION_TIME
    )
    refresh_token = authorize.create_refresh_token(
            subject=subject,
            algorithm=jwt_settings.ALGORITHM,
            expires_time=jwt_settings.REFRESH_TOKEN_EXPIRATION_TIME,
    )
    
    response.headers["access-control-expose-headers"] = "Set-Cookie"
    
    authorize.set_access_cookies(
        encoded_access_token=access_token,
        response=response,
        max_age=jwt_settings.ACCESS_TOKEN_EXPIRATION_TIME
    )
    authorize.set_refresh_cookies(
        encoded_refresh_token=refresh_token,
        response=response,
        max_age=jwt_settings.REFRESH_TOKEN_EXPIRATION_TIME
    )
