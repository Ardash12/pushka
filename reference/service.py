from sqlalchemy.orm import Session
from .models import Reference
from reference.schemas import CreateReference


def get_reference_list(db: Session):
    """Забираем из БД все объекты для GET запроса"""

    return db.query(Reference).all()


def post_reference(db: Session, item: CreateReference):
    """Записываем в БД данные из post запроса"""

    ref = Reference(**item.dict())
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return ref

