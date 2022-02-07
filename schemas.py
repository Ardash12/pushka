from pydantic import BaseModel
from datetime import datetime


class ReferenceStat(BaseModel):
    user_id: int
    event_id: int
    event_type: str
    click_time: datetime

    class Config:
        orm_mode = True
        
