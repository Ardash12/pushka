from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core import Base


class CategoryModel(Base):
    __tablename__ = "category"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
