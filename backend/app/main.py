from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.items import router as items_router

app = FastAPI(title="Production FastAPI Service")

app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(items_router, prefix="/items", tags=["Items"])
