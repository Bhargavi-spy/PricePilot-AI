from pydantic import BaseModel


class PriceSimulationRequest(BaseModel):
    cost_price: float
    selling_price: float
    stock: int


class PriceSimulationResponse(BaseModel):
    selling_price: float
    estimated_demand: str
    estimated_sales: int
    estimated_revenue: float
    estimated_profit: float
    recommendation: str