from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer)

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    quantity = Column(Integer)

Base.metadata.create_all(bind=engine)

# Pydantic Schemas
class SandwichCreate(BaseModel):
    name: str
    ingredients: str

class ResourceCreate(BaseModel):
    name: str
    quantity: int

class RecipeCreate(BaseModel):
    sandwich_id: int
    resource_id: int
    amount: int

class OrderDetailCreate(BaseModel):
    sandwich_id: int
    quantity: int

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Endpoints
@app.post("/sandwiches/")
def create_sandwich(sandwich: SandwichCreate, db: Session = Depends(get_db)):
    db_sandwich = Sandwich(name=sandwich.name, ingredients=sandwich.ingredients)
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

@app.get("/sandwiches/", response_model=List[SandwichCreate])
def read_sandwiches(db: Session = Depends(get_db)):
    return db.query(Sandwich).all()

@app.post("/resources/")
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(name=resource.name, quantity=resource.quantity)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@app.get("/resources/", response_model=List[ResourceCreate])
def read_resources(db: Session = Depends(get_db)):
    return db.query(Resource).all()

@app.post("/recipes/")
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = Recipe(sandwich_id=recipe.sandwich_id, resource_id=recipe.resource_id, amount=recipe.amount)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@app.get("/recipes/", response_model=List[RecipeCreate])
def read_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()

@app.post("/order_details/")
def create_order(order: OrderDetailCreate, db: Session = Depends(get_db)):
    db_order = OrderDetail(sandwich_id=order.sandwich_id, quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/order_details/", response_model=List[OrderDetailCreate])
def read_orders(db: Session = Depends(get_db)):
    return db.query(OrderDetail).all()
