from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers import recipes
from api.schemas import recipe as recipe_schema

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.post("/", response_model=recipe_schema.Recipe)
def create(data: recipe_schema.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, data=data)

@router.get("/", response_model=list[recipe_schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@router.get("/{item_id}", response_model=recipe_schema.Recipe)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = recipes.read_one(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return item

@router.put("/{item_id}", response_model=recipe_schema.Recipe)
def update(item_id: int, data: recipe_schema.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return recipes.delete(db, item_id)
