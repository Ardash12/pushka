from pydantic import BaseModel


class Catygory(BaseModel):
    name: str

    class Config:
        from_attributes = True