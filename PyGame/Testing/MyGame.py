from GameManager import GameManager

class MyGame:
    manager: GameManager = None

    @classmethod
    def Construct(cls, manager: GameManager):
        cls.manager = manager
        print("steve Construct")

    @staticmethod
    def Initialize():
        MyGame.Manager().BarManager.Initialize()
        print("steve Init")

    @staticmethod
    def LoadContent():
        print("steve LoadContent")

    @staticmethod
    def Update(gameTime: int):
        print(f"steve Update {gameTime}")

    @staticmethod
    def Draw():
        print("steve Draw")

    @classmethod
    def Manager(cls):
        return cls.manager