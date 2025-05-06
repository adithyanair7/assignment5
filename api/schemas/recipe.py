from pydantic import BaseModel, ConfigDict

class RecipeBase(BaseModel):
    pass

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
