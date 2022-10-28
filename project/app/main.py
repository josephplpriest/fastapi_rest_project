""" ~/app/main.py"""

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import get_settings, Settings


app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/marco")
async def polo(settings: Settings = Depends(get_settings)):
    "test if app works"
    
    return {
        "marco": "polo!",
        "environment": settings.environment,
        "testing": settings.testing
        }
