from pydantic import BaseModel


class Catygory(BaseModel):
    name: str

    class Config:
        orm_mode = True
