from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Static.Enumerations import ScreenType
from Static import Enumerations as enums


class DiffScreen(BaseScreen):

    def __init__(self):
        self.optionType: enums.OptionType = None
        self.nextScreen: enums.ScreenType = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()


    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()

        self.optionType: enums.OptionType = enums.OptionType.Invalid
        self.flag = False
        self.nextScreen = None


    def Update(self, deltaTime: int) -> ScreenType | None:
        if self.flag:
            super().BlockOnSoundFX()
            return self.nextScreen

        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            self.optionType: enums.OptionType = MyGame.Manager.InputManager.GetOptionType()
            if self.optionType != enums.OptionType.Invalid:
                MyGame.Manager.QuestionManager.SetDifficulty(self.optionType)
                MyGame.Manager.SoundManager.PauseMusic()
                MyGame.Manager.SoundManager.PlaySound(enums.SoundType.Right)
                self.nextScreen = ScreenType.Long
                self.flag = True
            else:
                back: bool = MyGame.Manager.InputManager.Back()
                if back:
                    MyGame.Manager.SoundManager.PauseMusic()
                    MyGame.Manager.SoundManager.PlaySound(enums.SoundType.Wrong)
                    self.nextScreen = ScreenType.Title
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
