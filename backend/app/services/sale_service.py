from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.repositories.sale_repository import SaleRepository
from app.schemas.sale_schema import SaleCreate


class SaleService:

    @staticmethod
    def create_sale(
        db: Session,
        request: SaleCreate
    ):

        product = ProductRepository.get_by_id(
            db,
            request.product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if request.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than zero"
            )

        if product.stock < request.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        return SaleRepository.create_sale(
            db,
            product,
            request.quantity
        )

    @staticmethod
    def get_all_sales(db: Session):
        return SaleRepository.get_all_sales(db)