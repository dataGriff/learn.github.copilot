from pydantic import BaseModel
from typing import List, Optional

class DistilleryBase(BaseModel):
    name: str
    location: str

class DistilleryCreate(DistilleryBase):
    pass

class Distillery(DistilleryBase):
    id: int
    whiskies: List[Optional[int]]  # Assuming whiskies are represented by their IDs

    class Config:
        orm_mode = True