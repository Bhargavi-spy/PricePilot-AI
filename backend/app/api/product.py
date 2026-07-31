from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.product_service import ProductService

from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

from app.schemas.profit_schema import ProfitResponse

from app.schemas.price_recommendation_schema import (
    PriceRecommendationRequest,
    PriceRecommendationResponse
)

from app.schemas.dashboard_schema import DashboardResponse
from app.schemas.low_stock_schema import LowStockResponse
from app.schemas.health_schema import InventoryHealthResponse


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# ---------------------------------------------------
# CREATE PRODUCT
# ---------------------------------------------------

@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return ProductService.create_product(db, product)


# ---------------------------------------------------
# GET ALL PRODUCTS (PAGINATION)
# ---------------------------------------------------

@router.get("/", response_model=list[ProductResponse])
def get_products(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return ProductService.get_paginated_products(db, page, size)


# ---------------------------------------------------
# SEARCH
# ---------------------------------------------------

@router.get("/search", response_model=list[ProductResponse])
def search_products(
    name: str = Query(..., description="Search product by name"),
    db: Session = Depends(get_db)
):
    return ProductService.search_products(db, name)


# ---------------------------------------------------
# FILTER
# ---------------------------------------------------

@router.get("/filter", response_model=list[ProductResponse])
def filter_products(
    category: str | None = Query(None),
    min_price: float | None = Query(None),
    max_price: float | None = Query(None),
    min_stock: int | None = Query(None),
    db: Session = Depends(get_db)
):
    return ProductService.filter_products(
        db,
        category,
        min_price,
        max_price,
        min_stock
    )


# ---------------------------------------------------
# SORT
# ---------------------------------------------------

@router.get("/sort", response_model=list[ProductResponse])
def sort_products(
    sort_by: str = Query(...),
    order: str = Query("asc"),
    db: Session = Depends(get_db)
):
    return ProductService.get_sorted_products(
        db,
        sort_by,
        order
    )


# ---------------------------------------------------
# LOW STOCK
# ---------------------------------------------------

@router.get(
    "/low-stock",
    response_model=list[LowStockResponse]
)
def get_low_stock_products(
    threshold: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    return ProductService.get_low_stock_products(
        db,
        threshold
    )


# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

@router.get(
    "/dashboard",
    response_model=DashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db)
):
    return ProductService.get_dashboard(db)


# ---------------------------------------------------
# INVENTORY HEALTH
# ---------------------------------------------------

@router.get(
    "/health",
    response_model=InventoryHealthResponse
)
def get_inventory_health(
    db: Session = Depends(get_db)
):
    return ProductService.get_inventory_health(db)


# ---------------------------------------------------
# PROFIT ANALYSIS
# ---------------------------------------------------

@router.get(
    "/{product_id}/profit",
    response_model=ProfitResponse
)
def get_profit_analysis(
    product_id: int,
    db: Session = Depends(get_db)
):
    analysis = ProductService.get_profit_analysis(
        db,
        product_id
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return analysis


# ---------------------------------------------------
# AI PRICE RECOMMENDATION
# ---------------------------------------------------

@router.post(
    "/recommend-price",
    response_model=PriceRecommendationResponse
)
def recommend_price(
    request: PriceRecommendationRequest
):
    return ProductService.recommend_price(request)


# ---------------------------------------------------
# GET PRODUCT BY ID
# ---------------------------------------------------

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = ProductService.get_product(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# ---------------------------------------------------
# UPDATE PRODUCT
# ---------------------------------------------------

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated = ProductService.update_product(
        db,
        product_id,
        product
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated


# ---------------------------------------------------
# DELETE PRODUCT
# ---------------------------------------------------

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    deleted = ProductService.delete_product(
        db,
        product_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }