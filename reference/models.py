from sqlalchemy import Column, String, Integer, Text, DateTime
from db import Base


class Reference(Base):
    __tablename__ = 'tablename_stat'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer)
    event_id = Column(Integer)
    event_type = Column(String)
    date = Column(DateTime)
