from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int = Field(..., description="Unique ID")
    username: str = Field(..., min_length=3, max_length=50, description="The username")
    #email: EmailStr = Field(..., description="User email addr")
    age: int = Field(..., gt=0)


try:
    user_data = {
        "id": 1,
        "username": "stevepro",
#        "email": "invalid_email",
        "age": -5
    }
    user = User(**user_data)
except Exception as e:
    print(e)
