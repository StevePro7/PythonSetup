from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


p = Point(10, 20)
print(p)                # Point(x=10, y=20)
