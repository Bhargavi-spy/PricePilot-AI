from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: str
    cost_price: float
    selling_price: float
    stock: int


# New Schema for Updating Products
class ProductUpdate(BaseModel):
    name: str
    category: str
    cost_price: float
    selling_price: float
    stock: int


class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }