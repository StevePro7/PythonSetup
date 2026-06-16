from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Static.Enumerations import ScreenType
from Static import Enumerations as enums


class InitScreen(BaseScreen):


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()


    def LoadContent(self) -> None:
        MyGame.Manager.SoundManager.PlayMusic(enums.MusicType.TitleMusic)


    def Update(self, deltaTime: int) -> ScreenType | None:
        return ScreenType.Title


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        super().DrawScreenText()
        super().HideCheatMode()
