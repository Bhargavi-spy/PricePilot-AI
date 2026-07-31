from pydantic import BaseModel


class InventoryHealthResponse(BaseModel):
    health_score: int
    status: str
    message: str
    total_products: int
    low_stock_products: int
    out_of_stock_products: int
    overstocked_products: int