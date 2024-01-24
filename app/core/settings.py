from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file='.env'
        env_file_encoding='utf-8'
    

class JWTSettings(Settings):
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRATION_TIME: int
    REFRESH_TOKEN_EXPIRATION_TIME: int
    COOKIE_SECURE: bool
    COOKIE_CSRF: bool
    COOKIE_SAMESITE: str
    COOKIE_DOMAIN: Optional[str] = None
    JWT_SECRET_KEY: str
    
jwt_settings = JWTSettings()
