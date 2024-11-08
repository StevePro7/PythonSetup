# tests/test_order.py
import unittest

from entities.customer import customer
from sales.schemas.models import Order
from aggregates.order import Order

class TestOrder(unittest.TestCase):
    def test_add_item(self):
        order = Order(order_id=1)
        order.add_item("Laptop", 1)
        order.add_item("Mouse", 2)
        self.assertEqual(order.total_items(), 2)
        self.assertEqual(order.items[0].product_name, "Laptop")

    def test_order_id(self):
        order = Order(order_id=2)
        self.assertEqual(order.order_id, 2)

if __name__ == '__main__':
    unittest.main()