import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager


app = FastAPI(debug=True)

class UserCreate:
    pass

class UserService:
    async def create(self, user: UserCreate):
        #await self._validate_email(user.email)
        #await self._check_exists(user.email)
        #return await self._save_user(user)
        await asyncio.sleep(2)
        pass

@app.post("/users")
async def create_user():
    #return await UserService().create(user)
    await asyncio.sleep(2)
