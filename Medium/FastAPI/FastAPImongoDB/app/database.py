from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DB_URL = "mongodb://localhost:27017"
MONGO_DB_NAME = "mydatabase"

client = AsyncIOMotorClient(MONGO_DB_URL)
database = client[MONGO_DB_NAME]
