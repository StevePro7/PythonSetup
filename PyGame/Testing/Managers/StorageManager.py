from MyGame import MyGame

class StorageManager:
    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")

    def LoadContent(self):
        MyGame.Manager.LogManager.Write("MGR Load")

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")

    def Draw(self):
        MyGame.Manager.LogManager.Write("MGR Draw")
