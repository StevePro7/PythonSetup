class Multiplier:
    def __init__(self, a, b, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: int):
        return (self.a * x**2) + (self.b * x**2) + (self.c * x**2)


func = Multiplier(2, 4, 6)
print(func(2))          # 48
print(func(4))          # 192
print(callable(func))   # True
