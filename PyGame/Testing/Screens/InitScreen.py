from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from Static.Assets import Assets
from enumerations import ScreenType


class InitScreen(BaseScreen):


    def Initialize(self) -> None:
        pass


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        MyGame.Manager.TextManager.DrawText("STEVEPRO", (0,0))
        MyGame.Manager.TextManager.DrawText("SUZANNE", (0, 20), (0, 255, 0))
        MyGame.Manager.TextManager.DrawText("ADRIANA", (0, 40), (0, 0, 255))
        pass
