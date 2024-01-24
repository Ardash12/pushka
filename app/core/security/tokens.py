from datetime import datetime, timedelta, timezone
from typing import Annotated, Union, cast

from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import Response
# from fastapi_jwt_auth import AuthJWT
from jose import JWTError, jwt

from app.core.settings import jwt_settings
from .settings import Settings


def create_access_token(response: Response, data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_settings.JWT_SECRET_KEY, algorithm=jwt_settings.ALGORITHM)
    
    print("GGGGG", encoded_jwt)
    
    response.set_cookie(key="access", value=encoded_jwt)
    
    return encoded_jwt

def get_token_from_cookie(request: Request):
    access_token = request.cookies.get('access')
    data = jwt.decode(token=access_token, key=jwt_settings.JWT_SECRET_KEY, algorithms=jwt_settings.ALGORITHM)
    print("GGGGGGG", data)
    return data


    
    
    


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, jwt_settings.JWT_SECRET_KEY, algorithms=[jwt_settings.ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


def set_and_create_tokens_cookies(
    response: Response, 
    subject: Union[int, str], 
    # authorize: AuthJWT = Depends(),
) -> None:
    pass
    # @AuthJWT.load_config
    # def get_config():
    #     return Settings()

    # access_token = authorize.create_access_token(
    #     subject=subject, 
    #     algorithm=jwt_settings.ALGORITHM,
    #     expires_time=jwt_settings.ACCESS_TOKEN_EXPIRATION_TIME
    # )
    # refresh_token = authorize.create_refresh_token(
    #         subject=subject,
    #         algorithm=jwt_settings.ALGORITHM,
    #         expires_time=jwt_settings.REFRESH_TOKEN_EXPIRATION_TIME,
    # )
    
    # response.headers["access-control-expose-headers"] = "Set-Cookie"
    
    # authorize.set_access_cookies(
    #     encoded_access_token=access_token,
    #     response=response,
    #     max_age=jwt_settings.ACCESS_TOKEN_EXPIRATION_TIME
    # )
    # authorize.set_refresh_cookies(
    #     encoded_refresh_token=refresh_token,
    #     response=response,
    #     max_age=jwt_settings.REFRESH_TOKEN_EXPIRATION_TIME
    # )
