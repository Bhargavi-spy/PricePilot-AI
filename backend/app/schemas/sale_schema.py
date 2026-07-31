from datetime import datetime
from pydantic import BaseModel


class SaleCreate(BaseModel):
    product_id: int
    quantity: int


class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    selling_price: float
    total_amount: float
    created_at: datetime

    class Config:
        from_attributes = True