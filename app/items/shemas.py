from typing import Optional

from pydantic import BaseModel


class ItemReviewSchema(BaseModel):
    grade: int
    item_id: Optional[int] = None
    
    
class ItemSchema(BaseModel):
    name: str
    description: Optional[str] = None
    reviews: Optional[list[ItemReviewSchema]] = None
