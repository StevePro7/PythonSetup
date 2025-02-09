from celery import Celery
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

celery = Celery("api", broker="redis://localhost:6379/0")


class Param(BaseModel):
    x: int
    y: int


@app.post("/add")
async def add(nums: Param):
    result = celery.send_task("add", queue="addition", kwargs=dict(nums))
    return {"task_id": result.id}


@app.post("/sub")
async def sub(nums: Param):
    result = celery.send_task("sub", queue="subtract", kwargs=dict(nums))
    return {"task_id", result.id}
