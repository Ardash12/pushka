from typing import Optional

from pydantic import BaseModel, EmailStr


class UserInfoResponse(BaseModel):
    id: int
    email: str
    
class SignInRequest(BaseModel):
    email: EmailStr
    password: str


class SignUpRequest(SignInRequest):
    ...
