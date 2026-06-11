import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType


class LongScreen(BaseScreen):

    def __init__(self):
        self.optionType: enumerations.OptionType = None
        self.nextScreen: enumerations.ScreenType = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()


    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()

        self.optionType: enumerations.OptionType = enumerations.OptionType.Invalid
        self.flag = False
        self.nextScreen = None


    def Update(self, deltaTime: int) -> ScreenType | None:
        if self.flag:
            super().BlockOnSoundFX()
            return self.nextScreen

        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            self.optionType: enumerations.OptionType = MyGame.Manager.InputManager.GetOptionType()
            if self.optionType != enumerations.OptionType.Invalid:
                MyGame.Manager.QuestionManager.SetQuizLength(self.optionType)
                MyGame.Manager.SoundManager.PauseMusic()
                MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Right)
                self.nextScreen = ScreenType.Ready
                self.flag = True
            else:
                back: bool = MyGame.Manager.InputManager.Back()
                if back:
                    MyGame.Manager.SoundManager.PauseMusic()
                    MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Wrong)
                    self.nextScreen = ScreenType.Diff
                    self.flag = True

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        super().DrawScreenText()
        super().HideCheatMode()

        MyGame.Manager.SpriteManager.DrawSelectAll()
        if self.flag:
            MyGame.Manager.SpriteManager.DrawRight(self.optionType)
