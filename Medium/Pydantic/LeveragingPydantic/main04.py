from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int = Field(..., description="Unique ID")
    username: str = Field(..., min_length=3, max_length=50, description="The username")
    #email: EmailStr = Field(..., description="User email addr")
    age: int = Field(..., gt=0)


app = FastAPI()
@app.post("/users/")
async def create_user(user: User):
    return {"message": "User created", "user":user.dict()}