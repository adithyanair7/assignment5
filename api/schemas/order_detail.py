from pydantic import BaseModel, ConfigDict

class OrderDetailBase(BaseModel):
    pass

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
