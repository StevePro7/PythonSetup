from payment_gateway import PaymentGateway
from order import Order

class OrderService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def process_order(self, order: Order) -> Order:
        # Process payment through the payment gateway
        if self.payment_gateway.process_payment(order.amount):
            order.process_order()
            return order
        else:
            raise ValueError("Payment failed.")
