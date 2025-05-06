from sqlalchemy import Column, Integer, Float, ForeignKey
from api.dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    amount_needed = Column(Float, nullable=False)
