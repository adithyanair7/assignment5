from pydantic import BaseModel
from typing import Optional

class OrderDetailBase(BaseModel):
    order_id: int
    sandwich_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    quantity: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True
