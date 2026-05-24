from MyGame import MyGame

class BarManager:

    def Initialize(self):
        pass

    def LoadContent(self):
        self.z = MyGame.Manager.FooManager.LoadContent()

    def TestValue(self) -> int:
        return self.z