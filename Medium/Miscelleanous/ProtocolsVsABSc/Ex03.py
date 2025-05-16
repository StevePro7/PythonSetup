from typing import Protocol

class Animal(Protocol):
    def eat(self, food) -> float:
        ...
    def sleep(self, hours) -> float:
        ...
