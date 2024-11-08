# shipping/models/order.py
class Order:
    def __init__(self, order_id, delivery_address, tracking_number):
        self.order_id = order_id
        self.delivery_address = delivery_address
        self.tracking_number = tracking_number

# Usage in Shipping context
shipping_order = Order(order_id=1, delivery_address="123 Main St", tracking_number="TRACK123")
print(f"Shipping Order: {shipping_order.delivery_address} - {shipping_order.tracking_number}")