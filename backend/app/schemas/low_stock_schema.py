from pydantic import BaseModel


class LowStockResponse(BaseModel):
    id: int
    name: str
    stock: int

    model_config = {
        "from_attributes": True
    }