from fastapi import APIRouter, HTTPException, Depends
from fastapi.param_functions import Body, Path
from fastapi.responses import Response
from fastapi_jwt_auth import AuthJWT
from starlette import status
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.users import UserModel, SignUpRequest, SignInRequest
from app.core import DatabaseSession
from app.core.security import (
    hash_password, 
    check_hashed_password, 
    set_and_create_tokens_cookies,
)


router = APIRouter()

# ====================================POST===================================

def sign_up_core(request: SignUpRequest, session: AsyncSession) -> None:
    session.execute(
        insert(UserModel).values(
            {
                UserModel.email: request.email.lower(),
                UserModel.password: hash_password(password=request.password),
            }
        )
    )
    session.commit()


@router.post(
    path='/sign_up',
    summary="WORKS: User registration.",
    status_code=status.HTTP_200_OK,
)
def sign_up(
    session: DatabaseSession,
    request: SignUpRequest = Body(...),
):
    if (session.execute(
        select(UserModel).where(UserModel.email == request.email.lower())
        )).scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email is already registered")
    sign_up_core(request=request, session=session)
    return {
        "ok": True,
        "result": True,
        "detail": {
            "message": "User is registered",
        },
    }
    
@router.post(
    path='/sign_in',
    summary="WORKS: User login (token creation).",
    status_code=status.HTTP_200_OK,
)
def sign_in(
    response: Response,
    session: DatabaseSession,
    authorize: AuthJWT = Depends(),
    request: SignInRequest = Body(),
):
    user = (
        session.execute(select(UserModel).where(UserModel.email == request.email.lower()))
    ).scalar_one_or_none()
    
    if not user or not check_hashed_password(password=request.password, hashed=user.password):
        raise HTTPException(status_code=403, detail="Email or password is incorrect")
    
    set_and_create_tokens_cookies(response=response, subject=user.id, authorize=authorize)
    
    return {
        "ok": True,
        "result": True,
    }