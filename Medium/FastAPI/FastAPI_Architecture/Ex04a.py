# api/users.py
from fastapi import APIRouter
router = APIRouter()


@router.get("/")
async def list_users():
    pass


@router.post("/")
async def create_user():
    pass


@router.get("/{user_id}")
async def get_user(user_id: str):
    pass
