from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate


class ProductRepository:

    # ---------------- CREATE ----------------

    @staticmethod
    def create(db: Session, product: ProductCreate):
        db_product = Product(
            name=product.name,
            category=product.category,
            cost_price=product.cost_price,
            selling_price=product.selling_price,
            stock=product.stock
        )

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product

    # ---------------- GET ALL ----------------

    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    # ---------------- GET BY ID ----------------

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    # ---------------- UPDATE ----------------

    @staticmethod
    def update(db: Session, product_id: int, product: ProductUpdate):

        db_product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not db_product:
            return None

        db_product.name = product.name
        db_product.category = product.category
        db_product.cost_price = product.cost_price
        db_product.selling_price = product.selling_price
        db_product.stock = product.stock

        db.commit()
        db.refresh(db_product)

        return db_product

    # ---------------- DELETE ----------------

    @staticmethod
    def delete(db: Session, product_id: int):

        db_product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not db_product:
            return None

        db.delete(db_product)
        db.commit()

        return True

    # ---------------- SEARCH ----------------

    @staticmethod
    def search_by_name(db: Session, name: str):
        return (
            db.query(Product)
            .filter(Product.name.ilike(f"%{name}%"))
            .all()
        )

    # ---------------- PAGINATION ----------------

    @staticmethod
    def get_paginated(db: Session, page: int, size: int):
        return (
            db.query(Product)
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

    # ---------------- SORT ----------------

    @staticmethod
    def get_sorted(db: Session, sort_by: str, order: str):

        allowed_columns = [
            "id",
            "name",
            "category",
            "cost_price",
            "selling_price",
            "stock"
        ]

        if sort_by not in allowed_columns:
            sort_by = "id"

        column = getattr(Product, sort_by)

        if order.lower() == "desc":
            return db.query(Product).order_by(column.desc()).all()

        return db.query(Product).order_by(column.asc()).all()

    # ---------------- FILTER ----------------

    @staticmethod
    def filter_products(
        db: Session,
        category: str = None,
        min_price: float = None,
        max_price: float = None,
        min_stock: int = None
    ):

        query = db.query(Product)

        if category:
            query = query.filter(
                Product.category.ilike(f"%{category}%")
            )

        if min_price is not None:
            query = query.filter(
                Product.selling_price >= min_price
            )

        if max_price is not None:
            query = query.filter(
                Product.selling_price <= max_price
            )

        if min_stock is not None:
            query = query.filter(
                Product.stock >= min_stock
            )

        return query.all()

    # ---------------- PROFIT DATA ----------------

    @staticmethod
    def get_profit_data(db: Session):
        return db.query(Product)

    @staticmethod
    def get_profit_data(db: Session, product_id: int):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    # ---------------- DASHBOARD ----------------

    @staticmethod
    def get_dashboard_data(db: Session):
        return db.query(Product).all()

    # ---------------- LOW STOCK ----------------

    @staticmethod
    def get_low_stock_products(
        db: Session,
        threshold: int = 10
    ):
        return (
            db.query(Product)
            .filter(Product.stock < threshold)
            .all()
        )

    # ---------------- INVENTORY STATISTICS ----------------

    @staticmethod
    def get_inventory_statistics(db: Session):

        total_products = db.query(Product).count()

        low_stock_products = (
            db.query(Product)
            .filter(Product.stock < 10)
            .count()
        )

        out_of_stock_products = (
            db.query(Product)
            .filter(Product.stock == 0)
            .count()
        )

        overstocked_products = (
            db.query(Product)
            .filter(Product.stock > 100)
            .count()
        )

        return {
            "total_products": total_products,
            "low_stock_products": low_stock_products,
            "out_of_stock_products": out_of_stock_products,
            "overstocked_products": overstocked_products
        }