from pydantic import BaseModel


class ProfitResponse(BaseModel):
    product_id: int
    product_name: str
    cost_price: float
    selling_price: float
    profit: float
    profit_margin: float