from typing import Optional

from pydantic import BaseModel


class ItemReviewSchema(BaseModel):
    id: int
    grade: int
    item_id: Optional[int] = None
    
    
class ItemSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    reviews: Optional[list[ItemReviewSchema]] = None
