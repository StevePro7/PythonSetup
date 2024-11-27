from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"


dog = Dog()
print(dog.sound())


# This lists all abstract methods a subclass MUST implement
# print(Animal.__abstractmethods__)