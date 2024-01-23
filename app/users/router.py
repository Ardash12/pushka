from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Body, Path
from starlette import status
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.users import UserModel, SignUpRequest
from app.core import DatabaseSession, hash_password


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
    status_code=status.HTTP_200_OK,
)
def sign_up(
    session: DatabaseSession,
    request: SignUpRequest = Body(...),
):
    if (session.execute(select(UserModel).where(UserModel.email == request.email.lower()))).scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email is already registered")
    sign_up_core(request=request, session=session)
    return {
        "ok": True,
        "result": True,
        "detail": {
            "message": "User is registered",
        },
    }
    