# 1. Core Features and Benefits
from fastapi import FastAPI

app = FastAPI(title="My FastAPI App", description="A simple API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
