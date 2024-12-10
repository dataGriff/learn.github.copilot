from pydantic import BaseModel
from typing import List, Optional

class WhiskyBase(BaseModel):
    name: str
    age: int
    distillery_id: int

class WhiskyCreate(WhiskyBase):
    pass

class Whisky(WhiskyBase):
    id: int

class WhiskyList(BaseModel):
    __root__: List[Whisky]