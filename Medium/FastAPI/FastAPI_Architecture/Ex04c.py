# main.py
from fastapi import FastAPI
import Ex04a
import Ex04b

app = FastAPI()
app.include_router(Ex04a.router, prefix="/users")
app.include_router(Ex04b.router, prefix="/orders")