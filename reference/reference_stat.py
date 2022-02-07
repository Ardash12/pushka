from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import get_db
from schemas import ReferenceStat
from . import service


router = APIRouter()


@router.get('/', response_model=List[ReferenceStat])
def ref_stat(db: Session = Depends(get_db)):
    return service.get_reference_list(db)


@router.post('/')
def ref_stat(item: ReferenceStat, db: Session = Depends(get_db)):
    return service.post_reference(db, item)

