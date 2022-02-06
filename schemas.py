from pydantic import BaseModel
from datetime import datetime


class Reference(BaseModel):
    user_id: int
    event_id: int
    event_type: str
    click_time: datetime
