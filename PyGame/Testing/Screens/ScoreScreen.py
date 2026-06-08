from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class ScoreScreen(BaseScreen):


    def Initialize(self) -> None:
        super().InitScreenText()


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        super().DrawScreenText()
