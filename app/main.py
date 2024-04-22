from fastapi import FastAPI
from app.database import engine

app = FastAPI()

from app.api import locations, categories, reviews, explore

from app.database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Map My World",
    description="API para explorar y revisar diferentes ubicaciones y categorías del mundo.",
    version="1.0.0"
)

app.include_router(categories.router, prefix="/api")
app.include_router(locations.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")
app.include_router(explore.router, prefix="/api")