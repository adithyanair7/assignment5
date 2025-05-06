from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers import order_details
from api.schemas import order_detail as order_detail_schema

router = APIRouter(prefix="/order_details", tags=["OrderDetails"])

@router.post("/", response_model=order_detail_schema.OrderDetail)
def create(data: order_detail_schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, data=data)

@router.get("/", response_model=list[order_detail_schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@router.get("/{item_id}", response_model=order_detail_schema.OrderDetail)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = order_details.read_one(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return item

@router.put("/{item_id}", response_model=order_detail_schema.OrderDetail)
def update(item_id: int, data: order_detail_schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return order_details.delete(db, item_id)
