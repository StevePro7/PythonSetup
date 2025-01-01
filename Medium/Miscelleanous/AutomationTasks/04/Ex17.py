# 17. Automate Currency Conversion
from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    return c. convert(from_currency, to_currency, amount)
