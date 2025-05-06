from sqlalchemy.orm import Session
from api.models.order import Order

def create(db: Session, data):
    db_item = Order(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(Order).all()

def read_one(db: Session, item_id: int):
    return db.query(Order).filter(Order.id == item_id).first()

def update(db: Session, item_id: int, data):
    db_item = db.query(Order).filter(Order.id == item_id)
    db_item.update(data.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(Order).filter(Order.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
