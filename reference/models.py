from sqlalchemy import Column, String, Integer, DateTime

from core.db import Base


class Reference(Base):
    __tablename__ = 'reference_stat'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer)
    event_id = Column(Integer)
    event_type = Column(String)
    date = Column(DateTime)
