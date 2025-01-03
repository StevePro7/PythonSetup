from pydantic import BaseModel
from bson import ObjectId

class Item(BaseModel):
    id: ObjectId
    name: str
    description: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }