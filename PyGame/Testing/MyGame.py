from GameManager import GameManager



class MyGame:
    manager: GameManager = None

    # THIS enables: MyGame.Manager
    class _ManagerProperty:
        def __get__(self, obj, owner):
            return owner.manager

    Manager = _ManagerProperty()

    @classmethod
    def Construct(cls, manager: GameManager):
        cls.manager = manager
        print("steve Construct")

    @classmethod
    def Initialize(cls):
        MyGame.Manager.BarManager.Initialize()
        MyGame.Manager.FooManager.Initialize()
        print("steve Init")

    @classmethod
    def LoadContent(cls):
        MyGame.Manager.BarManager.LoadContent()
        print("steve LoadContent")

    @staticmethod
    def Update(gameTime: int):
        print(f"steve Update {gameTime}")

    @classmethod
    def Draw(cls):
        print("steve Draw")


