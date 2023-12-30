from fastapi import APIRouter
from fastapi.param_functions import Body
from starlette import status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.categories import CategoryModel, CatygorySchema
from app.core import DatabaseSession


router = APIRouter()


def get_all_categories_core(session: AsyncSession):
    return(
        (session.execute(select(CategoryModel))).scalars().all()
    )


@router.get(
    path="/all",
    response_model=list[CatygorySchema],
    status_code=status.HTTP_200_OK,
)
def get_all_categories(session: DatabaseSession):
    return get_all_categories_core(session=session)


def add_category_core(session: AsyncSession, request):
    session.execute(
        insert(CategoryModel).values({
                    CategoryModel.name: request.name
                })
            )
    session.commit()


@router.post(
    path="/add",
    status_code=status.HTTP_201_CREATED,
)
def add_category(
    session: DatabaseSession,
    request: CatygorySchema = Body(...),
):
    add_category_core(session=session, request=request)
    return {
        "ok": True,
        "result": True,
    }
    