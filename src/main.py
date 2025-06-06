from fastapi import FastAPI
from src.routes.api import router as api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Emotion Analysis API"}

app.include_router(api_router)