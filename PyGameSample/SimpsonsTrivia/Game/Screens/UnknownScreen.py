from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Enumerations import ScreenType


class UnknownScreen(BaseScreen):


    def Initialize(self) -> None:
        pass


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        pass
