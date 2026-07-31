from pydantic import BaseModel


class PriceRecommendationRequest(BaseModel):
    cost_price: float
    selling_price: float
    stock: int
    demand: str


class PriceRecommendationResponse(BaseModel):
    current_price: float
    recommended_price: float
    price_change: str
    reason: str