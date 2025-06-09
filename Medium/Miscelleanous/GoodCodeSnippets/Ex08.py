Write

Sign in

You're reading for free via Mdabdullahalhasib's Friend Link. Become a member to access the best of Medium.

Member-only story
Mastering Python with These Code Snippets (Part 4)
Be an expert in OOP(Object Oriented Programming)
Mdabdullahalhasib
Mdabdullahalhasib
4 min read
·
Jan 31, 2025

Photo by Abhishek Prasad on Unsplash

If you are not a Medium Member, Please go to this link.

These code snippets will help you to improve your programming skills. Please run these codes in your code editor and also look at the comments. Let’s get started.
1. Classes, Objects, Attributes & Methods

    A class is a blueprint for creating objects that define the attributes, methods, and others.
    An Object is an instance of a class.
    Attributes are variables that belong to an object or class.
    Methods are functions that belong to an object or class.

class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

# Creating objects (instances of the Dog class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Output: Buddy
print(dog2.bark())  # Output: Max says woof!

2. Inheritance

It allows a class to inherit attributes and methods from the parent class.

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

3. Encapsulation

It restricts direct access to an object’s data and methods. It happens with private attributes (prefixed with _ or __) and getter or setter methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):  # Getter method
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

4. Polymorphism

It allows objects of different classes to be treated as objects of a common superclass.

class Bird:
    def speak(self):
        return "Chirp!"

class Duck(Bird):
    def speak(self):
        return "Quack!"

# common superclass
def animal_sound(animal):
    print(animal.speak())

bird = Bird()
duck = Duck()

animal_sound(bird)  # Output: Chirp!
animal_sound(duck)  # Output: Quack!

5. Abstraction

It is used to hide complex implementation details and expose only the necessary features. It defines a common interface for subclasses and enforces that certain methods must be implemented in subclasses. Here Circle is a subclass.

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5

6. Composition

It acts as an Inheritance but provides more flexibility and avoids the pitfalls of deep inheritance hierarchies.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Output: Engine started

7. Mixins

It provides methods to the other classes and is used to add functionality to classes.

class LoggingMixin:
    def log(self, message):
        print(f"Log: {message}")

class Vehicle(LoggingMixin):
    def __init__(self, name):
        self.name = name

    def start(self):
        self.log(f"{self.name} started")
        return "Vroom!"

car = Vehicle("Tesla")
print(car.start())  # Output: Log: Tesla started \n Vroom!

8. Slots for Memory Optimization

Python objects store their attributes in a dictionary that consumes much memory where __slots__ allow to explicitly define the attributes a class can have and reduce memory usage. If you want to add a new attribute outside slots, it will raise an error.

import sys

class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = WithoutSlots("Alice", 25)

print(sys.getsizeof(obj1.__dict__))  # Memory usage of __dict__
# 112  # Memory in bytes


class WithSlots:
    __slots__ = ['name', 'age']  # Restrict attributes to only 'name' and 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = WithSlots("Alice", 25)
obj2 = WithSlots("Bob", 30)

# print(obj1.__dict__)  # AttributeError: 'WithSlots' object has no attribute '__dict__'
print(sys.getsizeof(obj1))  # Memory usage of instance
#48  # Memory in bytes