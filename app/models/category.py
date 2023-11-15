from typing import Union
from sqlalchemy.orm import relationship
from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel
from app import Base


class CategoryModel(Base):
    __tablename__ = "category"
    
    name = Column(String)
    item = relationship("Item", back_populates="category")
    