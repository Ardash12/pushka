from typing import Union

from pydantic import BaseModel


class ItemResponse(BaseModel):
    name: str
    description: Union[str, None] = None
    