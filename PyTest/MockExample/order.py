class Order:
    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount
        self.status = "Pending"

    def process_order(self) -> str:
        if self.amount <= 0:
            raise ValueError("Order amount must be positive.")
        self.status = "Processed"
        return self.status



def foo() -> int:
    return 7