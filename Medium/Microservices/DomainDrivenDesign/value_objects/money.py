# value_objects/money.py
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

# Usage
payment1 = Money(100, 'USD')
payment2 = Money(100, 'USD')
print(payment1 == payment2)  # Output: True