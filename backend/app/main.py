from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.health import router as health_router
from app.database.database import create_tables

# Import models so SQLAlchemy knows about them
import app.models.product
from app.api.product import router as product_router
from app.api.sale import router as sale_router

app = FastAPI(
    title="PricePilot AI",
    description="AI-Powered Dynamic Pricing Optimization & Revenue Intelligence System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

app.include_router(health_router)
app.include_router(product_router)
app.include_router(sale_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to PricePilot AI",
        "status": "Running Successfully"
    }