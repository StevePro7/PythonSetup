# aggregates/order.py
class OrderItem:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, product_name, quantity):
        item = OrderItem(product_name, quantity)
        self.items.append(item)

    def total_items(self):
        return len(self.items)

# Usage
order = Order(order_id=1)
order.add_item("Laptop", 1)
order.add_item("Mouse", 2)
print(order.total_items())  # Output: 2