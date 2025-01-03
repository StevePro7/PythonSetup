#from motor.motor_asyncio import AsyncIOMotorClient
from . import models, schemas
from .database import database
from bson import ObjectId

async def create_item(item: schemas.ItemCreate):
    result = await database["items"].insert_one(item.dict())
    return {**item.dict(), "id": str(result.inserted_id)}

async def get_item(item_id: str):
    item = await database["items"].find_one({"_id": ObjectId(item_id)})
    return item

async def get_items(skip: int = 0, limit: int = 10):
    items = await database["items"].find().skip(skip).limit(limit).to_list(limit)
    return items
