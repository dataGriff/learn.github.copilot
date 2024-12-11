from pydantic import BaseModel
from fastapi import FastAPI
import hashlib
import base64
import os

class TextModel(BaseModel):
    text: str

    app = FastAPI()

    @app.post("/checksum")
    def get_checksum(text_model: TextModel):
        checksum = hashlib.md5(text_model.text.encode()).hexdigest()
        return {"checksum": checksum}
