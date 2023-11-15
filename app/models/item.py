from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

from app import Base


class ItemModel(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description: Column(String)
    category = relationship("Category", back_populates="item")
