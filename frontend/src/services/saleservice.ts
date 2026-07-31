import { api } from "./api";
import type { Sale } from "../types/sale";

export const getSales = async (): Promise<Sale[]> => {
  const response = await api.get<Sale[]>("/sales");
  return response.data;
};

export const createSale = async (
  sale: { product_id: number; quantity: number }
): Promise<Sale> => {
  const response = await api.post<Sale>("/sales", sale);
  return response.data;
};
