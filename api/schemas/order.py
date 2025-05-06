from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int

    class Config:
        from_attributes = True
