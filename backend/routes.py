from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
import requests

from backend.db import get_db
from backend.models import Travel
from backend.schemas import TravelCreate, TravelResponse

router = APIRouter(
    prefix="/travel",
    tags=["Travel"]
)

@router.get("/", response_model=list[TravelResponse])
def travel(db: Session = Depends(get_db)):
    travels = db.query(Travel).all()
    return travels

@router.post("/", response_model=TravelResponse)
def create_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    db_travel = Travel(**travel.dict())
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel


@router.delete("/{travel_id}")
def delete_travel(id: int, db: Session = Depends(get_db)):
    db_travel = db.query(Travel).filter(Travel.id == id).first()
    if not db_travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    db.delete(db_travel)
    db.commit()
    return Response(status_code=204)

@router.put("/{travel_id}")
def update_travel(id: int, travel: TravelCreate, db: Session = Depends(get_db)):
    db_travel = db.query(Travel).filter(Travel.id == id).first()
    if not db_travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    for key, value in travel.dict().items():
        setattr(db_travel, key, value)
    db.commit()
    db.refresh(db_travel)
    return db_travel
