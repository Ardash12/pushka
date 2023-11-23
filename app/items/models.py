from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core import Base


class ItemModel(Base):
    __tablename__ = "item"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
