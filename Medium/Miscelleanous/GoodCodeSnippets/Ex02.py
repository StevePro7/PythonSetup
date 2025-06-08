class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Method overriding
        return f"{self.name} says woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says woof!