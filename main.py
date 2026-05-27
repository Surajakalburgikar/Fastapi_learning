from fastapi import FastAPI
from src.utils.db import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "this is my tak managament application")

@app.get("/")
def home():
    return {"message": "hello"}