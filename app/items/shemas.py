from typing import Optional

from pydantic import BaseModel


class ItemSchema(BaseModel):
    name: str
    description: Optional[str] = None
    # reviews: Optional[list] = None
    