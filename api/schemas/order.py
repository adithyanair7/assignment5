from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    pass

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
