from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.sale_schema import (
    SaleCreate,
    SaleResponse
)
from app.services.sale_service import SaleService

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post(
    "/",
    response_model=SaleResponse
)
def create_sale(
    request: SaleCreate,
    db: Session = Depends(get_db)
):
    return SaleService.create_sale(
        db,
        request
    )


@router.get(
    "/",
    response_model=list[SaleResponse]
)
def get_sales(
    db: Session = Depends(get_db)
):
    return SaleService.get_all_sales(db)