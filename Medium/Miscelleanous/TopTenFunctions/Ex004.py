# 4. Map Function
def apply_discount(prices, discount):
    return list(map(lambda x: x * (1 - discount / 100), prices))

print(apply_discount([100, 200, 300, 400, 500], 10))