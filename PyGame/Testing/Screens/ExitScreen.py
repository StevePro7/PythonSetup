from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class ExitScreen(BaseScreen):

    def Initialize(self) -> None:
        self.actor = 0
        self.voice = str(self.actor)
        pass


    def LoadContent(self) -> None:
        pass


    def Update(self, deltaTime: int) -> ScreenType | None:
        test: bool = MyGame.Manager.InputManager.Advance()
        if test:
            self.actor += 1
            self.voice = str(self.actor)

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawActor(self.actor)
        MyGame.Manager.TextManager.DrawText(str(self.voice), 0, 0)
        pass
