""" ~/app/app.py"""

from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()

@app.get("/marco")
async def polo(settings: Settings = Depends(get_settings)):
    "test if app works"
    
    return {
        "marco": "polo!",
        "environment": settings.environment,
        "testing": settings.testing
        }
