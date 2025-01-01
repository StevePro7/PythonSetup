# 06. String Representation and Formatting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Person(name='{self.name}', age='{self.age}')"

p = Person("Alice", 30)
print(p)
print(str(p))
print(repr(p))