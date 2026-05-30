from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class OverScreen(BaseScreen):


    def Initialize(self) -> None:
        self.X: int = 0
        self.Y: int = 0


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        self.test: bool = MyGame.Manager.InputManager.GetOptionType()
        if self.test:
            self.X, self.Y = MyGame.Manager.InputManager.GetPosition()

        return None


    def Draw(self) -> None:
        for i in range(24):
            y = i * 20
            MyGame.Manager.TextManager.DrawText("X", (0, y))

        MyGame.Manager.TextManager.DrawText("SPLAT", (self.X, self.Y))
