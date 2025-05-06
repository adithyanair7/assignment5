from pydantic import BaseModel
from typing import Optional

class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    amount_needed: int

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount_needed: Optional[int] = None

class Recipe(RecipeBase):
    id: int

    class Config:
        from_attributes = True
