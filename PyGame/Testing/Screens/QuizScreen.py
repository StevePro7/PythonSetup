from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType
from enumerations import OptionType


class QuizScreen(BaseScreen):

    def Initialize(self) -> None:
        super().LoadScreenText()


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        super().DrawScreenText()
        MyGame.Manager.SpriteManager.DrawSelectAll()
        MyGame.Manager.SpriteManager.DrawRight(OptionType.A)
        #MyGame.Manager.SpriteManager.DrawWrong(OptionType.D)
        MyGame.Manager.SpriteManager.DrawVolumeOn()

