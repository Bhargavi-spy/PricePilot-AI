from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_products: int
    total_stock: int
    total_inventory_value: float
    potential_revenue: float
    expected_profit: float
    low_stock_products: int
    out_of_stock_products: int