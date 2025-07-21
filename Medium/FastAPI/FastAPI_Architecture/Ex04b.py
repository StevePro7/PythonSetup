# api/orders.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def list_orders():
    pass


@router.post("/")
async def create_order():
    pass
