from fastapi import APIRouter
from starlette import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import CategoryModel
router = APIRouter()


async def get_all_categories_core(session: AsyncSession):
    return (
        (await session.execute(select(CategoryModel))).scalars().all()
    )

@router.get(
    path="all/",
    response_model=None,
    status_code=status.HTTP_200_OK,
)
async def get_all_categories(session):
    return await get_all_categories_core(session=session)
