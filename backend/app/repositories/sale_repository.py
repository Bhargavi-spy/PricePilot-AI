from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.product import Product


class SaleRepository:

    @staticmethod
    def create_sale(
        db: Session,
        product: Product,
        quantity: int
    ):

        sale = Sale(
            product_id=product.id,
            quantity=quantity,
            selling_price=product.selling_price,
            total_amount=product.selling_price * quantity
        )

        db.add(sale)

        # Reduce stock
        product.stock -= quantity

        db.commit()
        db.refresh(sale)

        return sale

    @staticmethod
    def get_all_sales(db: Session):
        return db.query(Sale).all()