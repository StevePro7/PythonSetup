# sales_service/main.py
from fastapi import FastAPI
from sales.schemas.models import Order

app = FastAPI()

orders_db = []

@app.post("/orders/")
def create_order(order: Order):
    orders_db.append(order)
    return {"message": "Order created successfully", "order_id": order.order_id}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders_db:
        if order.order_id == order_id:
            return order
    return {"message": "Order not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
