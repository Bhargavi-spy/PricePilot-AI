from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    category = Column(String(100), nullable=False)

    cost_price = Column(Float, nullable=False)

    selling_price = Column(Float, nullable=False)

    stock = Column(Integer, default=0)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    sales = relationship(
        "Sale",
        back_populates="product",
        cascade="all, delete-orphan"
    )