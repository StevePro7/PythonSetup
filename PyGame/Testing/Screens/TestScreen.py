from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType
import constants as const


class TestScreen(BaseScreen):


    def Initialize(self) -> None:
        self.X: int = 2
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
            MyGame.Manager.TextManager.DrawText("X", 0, i)

        MyGame.Manager.TextManager.DrawText("SPLAT", int(self.X / const.FONT_SIZE), int(self. Y /const.FONT_SIZE))
