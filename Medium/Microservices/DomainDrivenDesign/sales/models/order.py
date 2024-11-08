# sales/models/order.py
class Order:
    def __init__(self, order_id, customer_name, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount

# Usage in Sales context
sales_order = Order(order_id=1, customer_name="John Doe", total_amount=150.0)
print(f"Sales Order: {sales_order.customer_name} - ${sales_order.total_amount}")