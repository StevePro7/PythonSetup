from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from enumerations import ScreenType


class DiffScreen(BaseScreen):


    def Initialize(self) -> None:
        screen = self.__class__.__name__
        self.textDataList: list[TextData] = MyGame.Manager.TextManager.LoadTextData(screen)


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        MyGame.Manager.TextManager.DrawTextDataList(self.textDataList)
