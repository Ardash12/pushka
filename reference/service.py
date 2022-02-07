from sqlalchemy.orm import Session
from .models import Reference
from schemas import ReferenceStat


def get_reference_list(db: Session):
    return db.query(Reference).all()


def post_reference(db: Session, item: ReferenceStat):
    ref = Reference(**item.dict())
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return ref

