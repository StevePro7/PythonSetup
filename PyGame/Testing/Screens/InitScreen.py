from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class InitScreen(BaseScreen):


    def Initialize(self) -> None:
        pass


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        MyGame.Manager.ContentManager.Draw()
