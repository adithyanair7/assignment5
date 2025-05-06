from pydantic import BaseModel, ConfigDict

class ResourceBase(BaseModel):
    pass

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
