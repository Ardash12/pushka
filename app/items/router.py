from fastapi import APIRouter
from fastapi.param_functions import Body, Path
from starlette import status
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from .models import ItemModel, ItemReviewModel
from .shemas import ItemRequest, ItemRespons, ItemReviewRequest
from app.core import DatabaseSession, hash_password


router = APIRouter()

# ====================================GET===================================

def get_all_items_core(session: AsyncSession):
    return (session.execute(select(ItemModel))).scalars().all()


@router.get(
    path='/all',
    response_model=list[ItemRespons],
    status_code=status.HTTP_200_OK,
)
def get_all_items(session: DatabaseSession):
    return get_all_items_core(session=session)


def get_item_core(session: AsyncSession, item_id: int) -> ItemModel:
    return (
        (
            session.execute(
                select(ItemModel)
                .where(ItemModel.id == item_id)
        )).scalar_one_or_none()
    )
    

@router.get(
    path='/{item_id}',
    response_model=ItemRespons,
    status_code=status.HTTP_200_OK,
)
def get_item(
    session: DatabaseSession,
    item_id: int = Path(...),
):
    return get_item_core(session=session, item_id=item_id)


# ====================================POST===================================

def add_items_core(session: AsyncSession, request):
    session.execute(
        insert(ItemModel).values({
                    ItemModel.name: request.name,
                    ItemModel.description: request.description,
                })
            )
    session.commit()


@router.post(
    path="/add",
    status_code=status.HTTP_201_CREATED,
)
def add_items(
    session: DatabaseSession,
    request: ItemRequest = Body(...),
):
    add_items_core(session=session, request=request)
    return {
        "ok": True,
        "result": True,
    }


def add_review_items_core(session: AsyncSession, request):
    session.execute(
        insert(ItemReviewModel).values({
                    ItemReviewModel.grade: request.grade,
                    ItemReviewModel.item_id: request.item_id,
                })
            )
    session.commit()


@router.post(
    path="/add_review",
    status_code=status.HTTP_201_CREATED,
)
def add_review_items(
    session: DatabaseSession,
    request: ItemReviewRequest = Body(...),
):
    add_review_items_core(session=session, request=request)
    return {
        "ok": True,
        "result": True,
    }
    