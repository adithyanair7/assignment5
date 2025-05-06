from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers import orders
from api.schemas import order as order_schema

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=order_schema.Order)
def create(data: order_schema.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, data=data)

@router.get("/", response_model=list[order_schema.Order])
def read_all(db: Session = Depends(get_db)):
    return orders.read_all(db)

@router.get("/{item_id}", response_model=order_schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = orders.read_one(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return item

@router.put("/{item_id}", response_model=order_schema.Order)
def update(item_id: int, data: order_schema.OrderUpdate, db: Session = Depends(get_db)):
    return orders.update(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return orders.delete(db, item_id)
