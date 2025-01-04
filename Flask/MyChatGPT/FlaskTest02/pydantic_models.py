from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr

    @validator("name")
    def validate_name(cls, v):
        if len(v) < 3:
            raise ValueError('Name must be at least 3 characters long')
        return v

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
