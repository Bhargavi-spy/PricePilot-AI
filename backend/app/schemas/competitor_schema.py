from pydantic import BaseModel


class CompetitorPriceRequest(BaseModel):
    product_name: str
    your_price: float
    amazon_price: float
    flipkart_price: float
    reliance_price: float


class CompetitorPriceResponse(BaseModel):
    average_market_price: float
    your_price: float
    difference: float
    recommendation: str
    reason: str