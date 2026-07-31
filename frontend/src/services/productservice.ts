import { api } from "./api";
import type { Product, ProductCreate } from "../types/product";

export const getProducts = async (
  page = 1,
  size = 10
): Promise<Product[]> => {
  const response = await api.get<Product[]>("/products", {
    params: { page, size },
  });
  return response.data;
};

export const searchProducts = async (name: string): Promise<Product[]> => {
  const response = await api.get<Product[]>("/products/search", {
    params: { name },
  });
  return response.data;
};

export const createProduct = async (
  product: ProductCreate
): Promise<Product> => {
  const response = await api.post<Product>("/products", product);
  return response.data;
};
