from Managers.BarManager import BarManager
from Managers.FooManager import FooManager


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
        BarManager: BarManager
        FooManager: FooManager