import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from enumerations import ScreenType


class DiffScreen(BaseScreen):

    def __init__(self):
        self.optionDelay: int = None
        self.cheatMode: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()
        self.optionDelay = MyGame.Manager.ConfigManager.ConfigData.OptionDelay
        self.cheatMode = MyGame.Manager.QuestionManager.GetCheatMode()


    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()


    def Update(self, deltaTime: int) -> ScreenType | None:
        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            optionType: enumerations.OptionType = MyGame.Manager.InputManager.GetOptionType()
            if optionType != enumerations.OptionType.Invalid:
                MyGame.Manager.QuestionManager.SetDifficulty(optionType)
                MyGame.Manager.SoundManager.PauseMusic()
                MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Right)
                super().BlockOnSoundFX()
                return enumerations.ScreenType.Long
            else:
                back: bool = MyGame.Manager.InputManager.Back()
                if back:
                    MyGame.Manager.SoundManager.PauseMusic()
                    MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Wrong)
                    super().BlockOnSoundFX()
                    return enumerations.ScreenType.Title

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        super().DrawScreenText()
        super().HideCheatMode()

        MyGame.Manager.SpriteManager.DrawSelectAll()
