from fastapi import APIRouter, HTTPException
from typing import List
from app.models.whisky import Whisky
from app.schemas.whisky import WhiskyCreate, Whisky as WhiskySchema

router = APIRouter()

# In-memory storage for whiskies (replace with database logic)
whiskies_db = []

@router.get("/", response_model=List[WhiskySchema])
async def list_whiskies():
    return whiskies_db

@router.post("/", response_model=WhiskySchema, status_code=201)
async def create_whisky(whisky: WhiskyCreate):
    new_whisky = Whisky(id=len(whiskies_db) + 1, **whisky.dict())
    whiskies_db.append(new_whisky)
    return new_whisky

@router.get("/{whisky_id}", response_model=WhiskySchema)
async def get_whisky_by_id(whisky_id: int):
    whisky = next((w for w in whiskies_db if w.id == whisky_id), None)
    if whisky is None:
        raise HTTPException(status_code=404, detail="Whisky not found")
    return whisky