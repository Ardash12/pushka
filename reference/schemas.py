from pydantic import BaseModel

from datetime import datetime


class ReferenceBase(BaseModel):
    user_id: int
    event_id: int
    event_type: str
    click_time: datetime


    class Config:
        orm_mode = True


# class ReferenceList(ReferenceBase):
#     id: int
