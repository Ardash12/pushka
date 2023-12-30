from typing import TYPE_CHECKING, Dict, List, Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core import Base


class ItemModel(Base):
    __tablename__ = "item"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str | None]
    reviews: Mapped[Optional[List["ItemReviewModel"]]] = relationship(
        back_populates="item"
    )


class ItemReviewModel(Base):
    __tablename__ = "item_review"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    grade_overall: Mapped[int]
    item_id = mapped_column(Integer, ForeignKey("item.id"))
    item: Mapped[Optional["ItemModel"]] = relationship(back_populates="reviews")
    