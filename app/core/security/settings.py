from typing import Set

from pydantic import BaseModel

from app.core.settings import jwt_settings


class Settings(BaseModel):
    authjwt_secret_key: str = jwt_settings.JWT_SECRET_KEY
    authjwt_token_location: Set[str] = {"cookies"}