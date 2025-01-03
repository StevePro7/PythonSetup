from fastapi import FastAPI, HTTPException, Depends
#from . import crud, models, schemas
import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import database #, get_db
from bson import ObjectId
from typing import List

app = FastAPI()

@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate):
    return await crud.create_item(item)

@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: str):
    item = await crud.get_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 10):
    items = await crud.get_items(skip, limit)
    return items


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)