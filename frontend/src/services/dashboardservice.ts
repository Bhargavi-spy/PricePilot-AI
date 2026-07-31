import { api } from "./api";
import type { DashboardResponse } from "../types/dashboard";
import type { LowStockProduct } from "../types/product";

export const getDashboard = async (): Promise<DashboardResponse> => {
  const response = await api.get<DashboardResponse>("/products/dashboard");
  return response.data;
};

export const getLowStockProducts = async (
  threshold = 10
): Promise<LowStockProduct[]> => {
  const response = await api.get<LowStockProduct[]>("/products/low-stock", {
    params: { threshold },
  });
  return response.data;
};
