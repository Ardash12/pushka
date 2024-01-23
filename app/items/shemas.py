from typing import Optional

from pydantic import BaseModel


# ====================================Respons===================================

class ItemReviewRespons(BaseModel):
    id: int
    grade: int
    item_id: Optional[int] = None
    
    
class ItemRespons(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    reviews: Optional[list[ItemReviewRespons]] = None
    
# ====================================Request===================================
    
class ItemReviewRequest(BaseModel):
    id: int
    grade: int
    item_id: Optional[int] = None
    
    
class ItemRequest(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    reviews: Optional[list[int]] = None
