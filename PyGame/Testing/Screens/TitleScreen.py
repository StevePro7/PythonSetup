from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class TitleScreen(BaseScreen):


    def Initialize(self) -> None:
        super().LoadScreenText()


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        #super().DrawScreenText()
