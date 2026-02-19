from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import engine, Base

# Import models (IMPORTANT: only import, no create_all per model)
from app.models import (
    user_model,
    item_model,
    order_model,
    order_item_model,
    audit_log_model,
)

# Import routers DIRECTLY (NO __init__.py usage)
from app.routes.auth_routes import router as auth_router
from app.routes.item_routes import router as item_router
from app.routes.order_routes import router as order_router
from app.routes.bill_routes import router as bill_router
from app.routes.audit_routes import router as audit_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create ALL tables ONCE
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(auth_router)
app.include_router(item_router)
app.include_router(order_router)
app.include_router(bill_router)
app.include_router(audit_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "status": "running",
        "debug": settings.DEBUG
    }
