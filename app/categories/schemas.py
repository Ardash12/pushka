from pydantic import BaseModel


class CatygorySchema(BaseModel):
    name: str

    class Config:
        from_attributes = True