# 2. Asynchronous Programming
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/async")
async def async_route():
    await asyncio.sleep(1)  # Simulating a long-running task
    return {"message": "This was handled asynchronously!"}
