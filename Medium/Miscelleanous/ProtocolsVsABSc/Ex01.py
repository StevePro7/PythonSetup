from abc import ABC, abstractmethod
from typing import Protocol

class Animal(ABC):
    @abstractmethod
    def eat(self, food) -> float:
        pass
    @abstractmethod
    def sleep(self, hourse) -> float:
        pass
