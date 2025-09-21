from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from routes import router as api_router
from database import db_manager

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Create the main app
app = FastAPI(title="Robert Chang Portfolio API", version="1.0.0")

# Include the API routes
app.include_router(api_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("Portfolio API server starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Portfolio API server shutting down...")
    await db_manager.close()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "portfolio-api"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Robert Chang Portfolio API", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)