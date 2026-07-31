export interface DashboardResponse {
  total_products: number;
  total_stock: number;
  total_inventory_value: number;
  potential_revenue: number;
  expected_profit: number;
  low_stock_products: number;
  out_of_stock_products: number;
}
