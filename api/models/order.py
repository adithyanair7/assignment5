from sqlalchemy import Column, Integer, String
from api.dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
