from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from core.utils import get_db
from reference.schemas import ReferenceBase, ReferenceList, CreateReference
# from reference import
from . import service


router = APIRouter()


@router.get('/', response_model=List[ReferenceList])
def ref_list(db: Session = Depends(get_db)):
    print(db)
    print(datetime.now())
    return service.get_reference_list(db)


@router.post('/')
def ref_list(item: CreateReference, db: Session = Depends(get_db)):
    print(db)
    return service.post_reference(db, item)
