from fastapi import APIRouter, HTTPException
from typing import List
from app.models.distillery import Distillery
from app.schemas.distillery import DistilleryCreate
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[Distillery])
def list_distilleries(db: Session = next(get_db())):
    return db.query(Distillery).all()

@router.post("/", response_model=Distillery, status_code=201)
def create_distillery(distillery: DistilleryCreate, db: Session = next(get_db())):
    new_distillery = Distillery(**distillery.dict())
    db.add(new_distillery)
    db.commit()
    db.refresh(new_distillery)
    return new_distillery

@router.get("/{distillery_id}", response_model=Distillery)
def get_distillery_by_id(distillery_id: int, db: Session = next(get_db())):
    distillery = db.query(Distillery).filter(Distillery.id == distillery_id).first()
    if not distillery:
        raise HTTPException(status_code=404, detail="Distillery not found")
    return distillery