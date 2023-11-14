from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    category: str