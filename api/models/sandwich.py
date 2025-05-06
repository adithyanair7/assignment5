from sqlalchemy import Column, Integer, String, Float
from api.dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
