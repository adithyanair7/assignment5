from pydantic import BaseModel, ConfigDict

class SandwichBase(BaseModel):
    pass

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
