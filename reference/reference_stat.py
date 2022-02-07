from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from reference.schemas import ReferenceBase
# from reference import
from . import service


router = APIRouter()


@router.get('/', response_model=List[ReferenceBase])
def ref_list(db: Session = Depends(get_db)):
    print(db)
    return {}
    # return service.get_reference_list(db)


# @router.post('/')
# def ref_stat(item: ReferenceBase, db: Session = Depends(get_db)):
#     return service.post_reference(db, item)

