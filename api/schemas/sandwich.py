from pydantic import BaseModel
from typing import Optional

class SandwichBase(BaseModel):
    name: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class Sandwich(SandwichBase):
    id: int

    class Config:
        from_attributes = True  # for ORM (SQLAlchemy) compatibility
