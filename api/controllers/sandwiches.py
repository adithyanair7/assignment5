from sqlalchemy.orm import Session
from api.models.sandwich import Sandwich
from api.schemas.sandwich import SandwichCreate, SandwichUpdate

def create(db: Session, data: SandwichCreate):
    item = Sandwich(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_all(db: Session):
    return db.query(Sandwich).all()

def read_one(db: Session, item_id: int):
    return db.query(Sandwich).filter(Sandwich.id == item_id).first()

def update(db: Session, item_id: int, data: SandwichUpdate):
    item = db.query(Sandwich).filter(Sandwich.id == item_id)
    item.update(data.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(Sandwich).filter(Sandwich.id == item_id)
    item.delete()
    db.commit()
