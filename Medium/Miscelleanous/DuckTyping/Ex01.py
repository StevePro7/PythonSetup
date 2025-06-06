from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class StevenProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} payment via Steven.")


processor = StevenProcessor()
processor.process_payment(100.0)