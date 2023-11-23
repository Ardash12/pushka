from fastapi import APIRouter
from fastapi.param_functions import Body
from starlette import status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import CategoryModel
from app.categories import Catygory
from app.core import DatabaseSession


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
async def get_all_categories(session: DatabaseSession):
    return await get_all_categories_core(session=session)


async def add_category_core(session: AsyncSession, request):
    return (
        (
            await session.execute(
                insert(CategoryModel)
                .values({
                    CategoryModel.name: 'cat1'
                })
            )
        )
    )


@router.post(
    path="add/",
    response_model=Catygory,
    status_code=status.HTTP_201_CREATED,
)
async def add_category(
    session: DatabaseSession,
    request: Catygory = Body(...),
):
    return await add_category_core(session=session, request=request)
    

