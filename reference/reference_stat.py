from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from reference.schemas import ReferenceList, CreateReference
from . import service


router = APIRouter()


@router.get('/', response_model=List[ReferenceList])
def ref_list(db: Session = Depends(get_db)):
    return service.get_reference_list(db)


@router.post('/')
def ref_list(item: CreateReference, db: Session = Depends(get_db)):
    return service.post_reference(db, item)
