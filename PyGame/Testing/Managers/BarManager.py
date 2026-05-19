from MyGame import MyGame

class BarManager:

    def Initialize(self):
        MyGame.Manager.LogManager.Write("BM steve Init")

    def LoadContent(self):
        MyGame.Manager.LogManager.Write("BM steve Load #1")
        MyGame.Manager.FooManager.LoadContent()
        MyGame.Manager.LogManager.Write("BM steve Load #2")

    def TestValue(self) -> int:
        return 7