from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class LocationCategoryReview(Base):
    __tablename__ = "location_category_reviews"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    rating = Column(Integer)
    last_review_date = Column(String(255))

    location = relationship("Location", back_populates="reviews")
    category = relationship("Category", back_populates="locations")

class LocationCategoryReviewCreate(BaseModel): 
    location_id: int
    category_id: int
    rating: int
    last_review_date: Optional[datetime] = None