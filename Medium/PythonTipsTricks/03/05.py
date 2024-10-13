class InverseStr:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __invert__(self) -> 'InverseStr':
        return InverseStr(self.value[::-1])

s = InverseStr('hello world')

print(s)   # hello world
print(~s)  # dlrow olleh