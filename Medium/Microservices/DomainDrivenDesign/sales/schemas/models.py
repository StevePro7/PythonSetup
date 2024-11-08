# sales_service/models.py
from typing import List
from pydantic import BaseModel

class OrderItem(BaseModel):
    product_name: str
    quantity: int

class Order(BaseModel):
    order_id: int
    customer_name: str
    items: List[OrderItem]