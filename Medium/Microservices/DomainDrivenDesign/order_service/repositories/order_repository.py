from order_service.models.order import Order

# repositories/order_repository.py
class OrderRepository:
    def __init__(self):
        self.orders = {}  # In-memory store for simplicity

    def add(self, myorder):
        self.orders[order.id] = myorder

    def get(self, order_id):
        return self.orders.get(order_id)

# Usage
repo = OrderRepository()
order = Order(id=1)
repo.add(order)
retrieved_order = repo.get(1)
print(retrieved_order.total_items())  # Output: 0