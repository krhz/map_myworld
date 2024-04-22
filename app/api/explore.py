from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models.location import Location
from app.models.category import Category
from app.models.location_category_review import LocationCategoryReview

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/explore")
def explore_locations_categories(db: Session = Depends(get_db)):

    thirty_days_ago = datetime.utcnow() - timedelta(days=30)

    unreviewed_combinations = (
        db.query(Location.id.label("location_id"),
                 Location.latitude.label("location_latitude"),
                 Location.longitude.label("location_longitude"),
                 Category.id.label("category_id"),
                 Category.name.label("category_name"),
                 LocationCategoryReview.rating.label("review_rating"),
                 LocationCategoryReview.id.label("review_id"),
                 LocationCategoryReview.last_review_date.label("last_review_date"))
        .select_from(Location)
        .outerjoin(LocationCategoryReview,
                   (Location.id == LocationCategoryReview.location_id))
        .outerjoin(Category,
                   (Category.id == LocationCategoryReview.category_id))
        .filter(LocationCategoryReview.last_review_date <= thirty_days_ago)
        .distinct(Location.id, Category.id)
        .limit(10)
        .all()
    )

    unreviewed_unique_combinations = []

    for row in unreviewed_combinations:
        location_id = row.location_id
        location_latitude = row.location_latitude
        location_longitude = row.location_longitude
        category_id = row.category_id
        category_name = row.category_name
        rating = row.review_rating
        review_id = row.review_id
        last_review_date = row.last_review_date
        
        
        unreviewed_unique_combinations.append({
            "review_id": review_id,
            "location_id": location_id,
            "location_latitude": location_latitude,
            "location_longitude": location_longitude,
            "category_id": category_id,
            "category_name": category_name,
            "rating": rating,
            "last_review_date": last_review_date,
        })

    return unreviewed_unique_combinations