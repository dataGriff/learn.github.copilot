from fastapi import FastAPI
from app.api import distilleries, whiskies

app = FastAPI(title="Distillery and Whisky Inventory API", version="1.0.0")

app.include_router(distilleries.router, prefix="/distilleries", tags=["Distilleries"])
app.include_router(whiskies.router, prefix="/whiskies", tags=["Whiskies"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Distillery and Whisky Inventory API"}