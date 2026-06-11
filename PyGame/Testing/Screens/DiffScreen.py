import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from enumerations import ScreenType


class DiffScreen(BaseScreen):

    def __init__(self):
        self.optionDelay: int = None
        self.cheatMode: bool = None
        self.optionType: enumerations.OptionType = None
        self.nextScreen: enumerations.ScreenType = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()
        self.optionDelay = MyGame.Manager.ConfigManager.ConfigData.OptionDelay



    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()

        self.cheatMode = MyGame.Manager.QuestionManager.GetCheatMode()
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
                MyGame.Manager.QuestionManager.SetDifficulty(self.optionType)
                MyGame.Manager.SoundManager.PauseMusic()
                MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Right)
                self.nextScreen = ScreenType.Long
                self.flag = True
            else:
                back: bool = MyGame.Manager.InputManager.Back()
                if back:
                    MyGame.Manager.SoundManager.PauseMusic()
                    MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Wrong)
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
