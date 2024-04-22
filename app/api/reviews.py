from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.location import Location
from app.models.category import Category
from app.models.location_category_review import LocationCategoryReview, LocationCategoryReviewCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/locations/{location_id}/reviews")
def get_location_reviews(location_id: int, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    
    reviews = location.reviews
    return reviews

@router.get("/reviews")
def get_location_reviews(location_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Location).all()
    return reviews


@router.post("/reviews")
def create_location_category_review(review_data: LocationCategoryReviewCreate, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == review_data.location_id).first()
    category = db.query(Category).filter(Category.id == review_data.category_id).first()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    new_review = LocationCategoryReview(
        location_id=review_data.location_id,
        category_id=review_data.category_id,
        rating=review_data.rating
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

@router.put("/reviews/{id}/review_date")
def update_last_review_date(id: int, db: Session = Depends(get_db)):
    review = db.query(LocationCategoryReview).filter(LocationCategoryReview.id == id).first()

    if not review:
        raise HTTPException(status_code=404, detail="Location-Category review not found")

    review.last_review_date = datetime.utcnow()

    db.commit()

    return {"message": "Last review date updated successfully"}