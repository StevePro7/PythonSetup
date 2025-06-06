from typing import Protocol

class PaymentProcessor(Protocol):
    def process_payment(self, amount: float) -> None:
        pass


class StevenProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Steven.")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Stripe.")

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Crypto.")

def handle_payment(processor: PaymentProcessor, amount: float) -> None:
    processor.process_payment(amount)

steven = StevenProcessor()
stripe = StripeProcessor()
crypto = CryptoProcessor()

handle_payment(steven, 100.0)
handle_payment(stripe, 200.0)
handle_payment(crypto, 300.0)