from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.location import Location

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/locations", status_code=200)
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(Location).all()
    return locations


@router.post("/locations", status_code=201)
def create_location(location_data: dict, db: Session = Depends(get_db)):
    new_location = Location(**location_data)
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location
