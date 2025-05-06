from sqlalchemy.orm import Session
from api.models.resource import Resource
from api.schemas.resource import ResourceCreate, ResourceUpdate

def create(db: Session, data: ResourceCreate):
    item = Resource(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def read_all(db: Session):
    return db.query(Resource).all()

def read_one(db: Session, item_id: int):
    return db.query(Resource).filter(Resource.id == item_id).first()

def update(db: Session, item_id: int, data: ResourceUpdate):
    item = db.query(Resource).filter(Resource.id == item_id)
    item.update(data.model_dump(exclude_unset=True))
    db.commit()
    return item.first()

def delete(db: Session, item_id: int):
    item = db.query(Resource).filter(Resource.id == item_id)
    item.delete()
    db.commit()
