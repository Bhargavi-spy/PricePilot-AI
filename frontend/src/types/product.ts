export interface Product {
  id: number;
  name: string;
  category: string;
  cost_price: number;
  selling_price: number;
  stock: number;
}

export interface ProductCreate {
  name: string;
  category: string;
  cost_price: number;
  selling_price: number;
  stock: number;
}

export interface LowStockProduct {
  id: number;
  name: string;
  stock: number;
}
