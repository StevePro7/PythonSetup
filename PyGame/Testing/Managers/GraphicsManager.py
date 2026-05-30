from MyGame import MyGame
from Static.Assets import Assets

class GraphicsManager:
    def Initialize(self):
        # MyGame.Manager.LogManager.Write("MGR init")
        pass

    def LoadContent(self):
        # MyGame.Manager.LogManager.Write("MGR Load")
        return None

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")

    def Draw(self):
        surface = Assets.EmulogicFont.render("STEVEPRO", False, (255, 0, 0))
        MyGame.Manager.DisplayManager.Foo(surface)
