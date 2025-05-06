from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers import sandwichs
from api.schemas import sandwich as sandwich_schema

router = APIRouter(prefix="/sandwichs", tags=["Sandwichs"])

@router.post("/", response_model=sandwich_schema.Sandwich)
def create(data: sandwich_schema.SandwichCreate, db: Session = Depends(get_db)):
    return sandwichs.create(db=db, data=data)

@router.get("/", response_model=list[sandwich_schema.Sandwich])
def read_all(db: Session = Depends(get_db)):
    return sandwichs.read_all(db)

@router.get("/{item_id}", response_model=sandwich_schema.Sandwich)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = sandwichs.read_one(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return item

@router.put("/{item_id}", response_model=sandwich_schema.Sandwich)
def update(item_id: int, data: sandwich_schema.SandwichUpdate, db: Session = Depends(get_db)):
    return sandwichs.update(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return sandwichs.delete(db, item_id)
