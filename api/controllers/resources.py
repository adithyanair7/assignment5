from sqlalchemy.orm import Session
from api.models.resource import Resource

def create(db: Session, data):
    db_item = Resource(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(Resource).all()

def read_one(db: Session, item_id: int):
    return db.query(Resource).filter(Resource.id == item_id).first()

def update(db: Session, item_id: int, data):
    db_item = db.query(Resource).filter(Resource.id == item_id)
    db_item.update(data.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(Resource).filter(Resource.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
