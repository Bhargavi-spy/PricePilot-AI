from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository

from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.schemas.profit_schema import ProfitResponse
from app.schemas.price_recommendation_schema import (
    PriceRecommendationRequest,
    PriceRecommendationResponse
)
from app.schemas.dashboard_schema import DashboardResponse
from app.schemas.low_stock_schema import LowStockResponse
from app.schemas.health_schema import InventoryHealthResponse


class ProductService:

    # ---------------- CREATE ----------------

    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        return ProductRepository.create(db, product)

    # ---------------- PAGINATION ----------------

    @staticmethod
    def get_paginated_products(db: Session, page: int, size: int):
        return ProductRepository.get_paginated(db, page, size)

    # ---------------- SEARCH ----------------

    @staticmethod
    def search_products(db: Session, name: str):
        return ProductRepository.search_by_name(db, name)

    # ---------------- SORT ----------------

    @staticmethod
    def get_sorted_products(db: Session, sort_by: str, order: str):
        return ProductRepository.get_sorted(db, sort_by, order)

    # ---------------- FILTER ----------------

    @staticmethod
    def filter_products(
        db: Session,
        category: str = None,
        min_price: float = None,
        max_price: float = None,
        min_stock: int = None
    ):
        return ProductRepository.filter_products(
            db,
            category,
            min_price,
            max_price,
            min_stock
        )

    # ---------------- GET BY ID ----------------

    @staticmethod
    def get_product(db: Session, product_id: int):
        return ProductRepository.get_by_id(db, product_id)

    # ---------------- UPDATE ----------------

    @staticmethod
    def update_product(db: Session, product_id: int, product: ProductUpdate):
        return ProductRepository.update(db, product_id, product)

    # ---------------- DELETE ----------------

    @staticmethod
    def delete_product(db: Session, product_id: int):
        return ProductRepository.delete(db, product_id)

    # ---------------- PROFIT ANALYSIS ----------------

    @staticmethod
    def get_profit_analysis(db: Session, product_id: int):

        product = ProductRepository.get_profit_data(db, product_id)

        if not product:
            return None

        profit = product.selling_price - product.cost_price
        profit_margin = (profit / product.selling_price) * 100

        return ProfitResponse(
            product_id=product.id,
            product_name=product.name,
            cost_price=product.cost_price,
            selling_price=product.selling_price,
            profit=round(profit, 2),
            profit_margin=round(profit_margin, 2)
        )

    # ---------------- AI PRICE RECOMMENDATION ----------------

    @staticmethod
    def recommend_price(request: PriceRecommendationRequest):

        current_price = request.selling_price
        cost_price = request.cost_price
        stock = request.stock
        demand = request.demand.lower()

        recommended_price = current_price

        profit = current_price - cost_price
        profit_margin = (profit / current_price) * 100

        reasons = []

        # HIGH DEMAND
        if demand == "high":

            if stock < 20:
                recommended_price *= 1.12
                reasons.append("Very low stock")

            elif stock < 50:
                recommended_price *= 1.08
                reasons.append("Limited stock")

            else:
                recommended_price *= 1.05
                reasons.append("High demand")

        # MEDIUM DEMAND
        elif demand == "medium":

            if stock > 150:
                recommended_price *= 0.98
                reasons.append("Large inventory")

            else:
                recommended_price *= 1.02
                reasons.append("Stable demand")

        # LOW DEMAND
        elif demand == "low":

            if stock > 200:
                recommended_price *= 0.85
                reasons.append("Excess inventory")

            elif stock > 100:
                recommended_price *= 0.90
                reasons.append("High inventory")

            else:
                recommended_price *= 0.95
                reasons.append("Low demand")

        # Profit margin check
        if profit_margin < 10:
            recommended_price *= 1.05
            reasons.append("Profit margin too low")

        elif profit_margin > 40:
            recommended_price *= 0.97
            reasons.append("Very high margin")

        # Never sell below cost +5%
        minimum_price = cost_price * 1.05

        if recommended_price < minimum_price:
            recommended_price = minimum_price
            reasons.append("Protected minimum profit")

        price_difference = recommended_price - current_price
        percent_change = (price_difference / current_price) * 100

        if abs(percent_change) < 0.1:
            price_change = "0%"
        elif percent_change > 0:
            price_change = f"+{round(percent_change,2)}%"
        else:
            price_change = f"{round(percent_change,2)}%"

        return PriceRecommendationResponse(
            current_price=current_price,
            recommended_price=round(recommended_price, 2),
            price_change=price_change,
            reason=", ".join(reasons)
        )

    # ---------------- DASHBOARD ----------------

    @staticmethod
    def get_dashboard(db: Session):

        products = ProductRepository.get_dashboard_data(db)

        total_products = len(products)

        total_stock = sum(product.stock for product in products)

        total_inventory_value = sum(
            product.cost_price * product.stock
            for product in products
        )

        potential_revenue = sum(
            product.selling_price * product.stock
            for product in products
        )

        expected_profit = potential_revenue - total_inventory_value

        low_stock_products = sum(
            1 for product in products if product.stock < 10
        )

        out_of_stock_products = sum(
            1 for product in products if product.stock == 0
        )

        return DashboardResponse(
            total_products=total_products,
            total_stock=total_stock,
            total_inventory_value=round(total_inventory_value, 2),
            potential_revenue=round(potential_revenue, 2),
            expected_profit=round(expected_profit, 2),
            low_stock_products=low_stock_products,
            out_of_stock_products=out_of_stock_products
        )

    # ---------------- LOW STOCK ----------------

    @staticmethod
    def get_low_stock_products(
        db: Session,
        threshold: int = 10
    ):

        products = ProductRepository.get_low_stock_products(
            db,
            threshold
        )

        return [
            LowStockResponse(
                id=product.id,
                name=product.name,
                stock=product.stock
            )
            for product in products
        ]

    # ---------------- INVENTORY HEALTH ----------------

    @staticmethod
    def get_inventory_health(db: Session):

        stats = ProductRepository.get_inventory_statistics(db)

        total = stats["total_products"]

        if total == 0:
            return InventoryHealthResponse(
                health_score=100,
                status="Excellent",
                message="No products available.",
                total_products=0,
                low_stock_products=0,
                out_of_stock_products=0,
                overstocked_products=0
            )

        score = 100

        score -= stats["low_stock_products"] * 5
        score -= stats["out_of_stock_products"] * 10
        score -= stats["overstocked_products"] * 3

        score = max(0, min(score, 100))

        if score >= 90:
            status = "Excellent"
            message = "Inventory is in excellent condition."

        elif score >= 75:
            status = "Good"
            message = "Inventory is healthy."

        elif score >= 50:
            status = "Average"
            message = "Inventory needs attention."

        else:
            status = "Poor"
            message = "Inventory requires immediate action."

        return InventoryHealthResponse(
            health_score=score,
            status=status,
            message=message,
            total_products=stats["total_products"],
            low_stock_products=stats["low_stock_products"],
            out_of_stock_products=stats["out_of_stock_products"],
            overstocked_products=stats["overstocked_products"]
        )