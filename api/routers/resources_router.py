from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers import resources
from api.schemas import resource as resource_schema

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/", response_model=resource_schema.Resource)
def create(data: resource_schema.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, data=data)

@router.get("/", response_model=list[resource_schema.Resource])
def read_all(db: Session = Depends(get_db)):
    return resources.read_all(db)

@router.get("/{item_id}", response_model=resource_schema.Resource)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = resources.read_one(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return item

@router.put("/{item_id}", response_model=resource_schema.Resource)
def update(item_id: int, data: resource_schema.ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return resources.delete(db, item_id)
