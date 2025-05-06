from pydantic import BaseModel
from typing import Optional

class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None

class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True
