from sqlalchemy.orm import Session
from api.models.recipe import Recipe
from api.schemas.recipe import RecipeCreate, RecipeUpdate

def create(db: Session, data: RecipeCreate):
    item = Recipe(sandwich_id=data.sandwich_id,
        resource_id=data.resource_id,
        amount_needed=data.amount_needed)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_all(db: Session):
    return db.query(Recipe).all()

def read_one(db: Session, item_id: int):
    return db.query(Recipe).filter(Recipe.id == item_id).first()

def update(db: Session, item_id: int, data: RecipeUpdate):
    item = db.query(Recipe).filter(Recipe.id == item_id)
    item.update(data.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(Recipe).filter(Recipe.id == item_id)
    item.delete()
    db.commit()
