from typing import Union

from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()

class ItemModel(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description: Column(String)
    category = relationship("Category", back_populates="item")