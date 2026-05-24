from MyGame import MyGame

class FooManager:
    def Initialize(self):
        # MyGame.Manager.LogManager.Write("MGR init")
        pass

    def LoadContent(self):
        # MyGame.Manager.LogManager.Write("MGR Load")
        pass

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")

    def Draw(self):
        MyGame.Manager.LogManager.Write("MGR Draw")
