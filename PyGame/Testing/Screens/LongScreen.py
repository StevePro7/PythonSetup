from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class LongScreen(BaseScreen):

    def Initialize(self) -> None:
        self.text: str = None
        self.Y: int = 0


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        self.test: bool = MyGame.Manager.InputManager.Advance()
        if self.test:
            self.Y += 20
        return None


    def Draw(self) -> None:
        for i in range(24):
            y = i * 20
            MyGame.Manager.TextManager.DrawText("X", (0, y))

        MyGame.Manager.TextManager.DrawText("SPACE", (40, self.Y))
        pass
