# services/order_service.py
class OrderService:
    def calculate_total(self, order):
        return sum(item.quantity * 10 for item in order.items)  # Assume each item is $10

# tests/test_order_service.py
import unittest
from aggregates.order import Order

class TestOrderService(unittest.TestCase):
    def test_calculate_total(self):
        order = Order(order_id=1)
        order.add_item("Laptop", 2)
        order.add_item("Mouse", 1)
        service = OrderService()
        total = service.calculate_total(order)
        self.assertEqual(total, 30)  # 2 Laptops + 1 Mouse = 30

if __name__ == '__main__':
    unittest.main()