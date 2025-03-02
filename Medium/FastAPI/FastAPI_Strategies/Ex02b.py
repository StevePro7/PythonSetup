import aioredis
from fastapi import FastAPI

app = FastAPI()
redis = aioredis.from_url("redis://localhost")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cached_item = await redis.get(f"item:{item_id}")
    if cached_item:
        return {"item": cached_item.decode("utf-8")}
    # Else, fetch from the database or compute the result
    #item = await fetch_item_from_db(item_id)
    item = 42
    await redis.set(f"item:{item_id}", item, ex=300)  # Cache for 5 minutes
    return {"item": item}