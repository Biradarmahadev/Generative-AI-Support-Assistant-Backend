from fastapi import FastAPI
from app.utils.logger import logger
from app.config import settings
from app.routes.support import router as support_router

app = FastAPI(title="AI Support Assistant Backend")

app.include_router(support_router)

@app.get("/")
def health():
    logger.info("Health check endpoint called")
    return {
        "status": "Backend is running 🚀",
        "environment": settings.APP_ENV
    }
