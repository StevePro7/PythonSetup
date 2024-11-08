# events/order_placed.py
from datetime import datetime

class OrderPlaced:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"OrderPlaced(order_id={self.order_id}, customer={self.customer_name}, amount={self.amount})"