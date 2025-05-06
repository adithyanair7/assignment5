from sqlalchemy.orm import Session
from api.models.order_detail import OrderDetail
from api.schemas.order_detail import OrderDetailCreate, OrderDetailUpdate

def create(db: Session, data: OrderDetailCreate):
    item = OrderDetail(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_all(db: Session):
    return db.query(OrderDetail).all()

def read_one(db: Session, item_id: int):
    return db.query(OrderDetail).filter(OrderDetail.id == item_id).first()

def update(db: Session, item_id: int, data: OrderDetailUpdate):
    item = db.query(OrderDetail).filter(OrderDetail.id == item_id)
    item.update(data.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(OrderDetail).filter(OrderDetail.id == item_id)
    item.delete()
    db.commit()
