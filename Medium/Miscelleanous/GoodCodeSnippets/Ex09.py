from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Alice", 25)
print(p1)  # Person(name='Alice', age=25)