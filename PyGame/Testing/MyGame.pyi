from FooManager import FooManager
from BarManager import BarManager


class MyGame:
    @staticmethod
    def Construct(): ...

    @staticmethod
    def Initialize(): ...

    @staticmethod
    def LoadContent(): ...

    @staticmethod
    def Update(game_time: float): ...

    @staticmethod
    def Draw(): ...

    class Manager:
        ...
        FooManager: FooManager
        BarManager: BarManager