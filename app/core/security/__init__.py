from typing import Optional
from typing_extensions import Annotated

from fastapi.param_functions import Depends

from app.users import UserModel

from .authorization import authorization_optional
from .pwd_hashing import hash_password, check_hashed_password
from .tokens import set_and_create_tokens_cookies, get_access_token_from_cookie
from .settings import Settings

AuthorizationOptional = Annotated[Optional[UserModel], Depends(authorization_optional)]

__all__ = (
    "AuthorizationOptional",
    "check_hashed_password",
    "get_access_token_from_cookie",
    "hash_password",
    "set_and_create_tokens_cookies",
    "Settings",
)
