from sqlalchemy.orm import Session
from api.models.order import Order
from api.schemas.order import OrderCreate, OrderUpdate

def create(db: Session, data: OrderCreate):
    item = Order(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_all(db: Session):
    return db.query(Order).all()

def read_one(db: Session, item_id: int):
    return db.query(Order).filter(Order.id == item_id).first()

def update(db: Session, item_id: int, data: OrderUpdate):
    item = db.query(Order).filter(Order.id == item_id)
    item.update(data.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(Order).filter(Order.id == item_id)
    item.delete()
    db.commit()
