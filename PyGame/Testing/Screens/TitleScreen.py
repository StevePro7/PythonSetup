import pygame

import constants
import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class TitleScreen(BaseScreen):

    def __init__(self):
        self.titleDelay: int = None
        self.flash: bool = None
        self.globalCheat: bool = None
        self.localCheat: bool = None
        self.cheatCount: int = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()

        self.textPositions: list[pygame.Vector2] = self.__getTextPositions()
        self.whitePositions: list[pygame.Vector2] = self.__getWhitePositions()

        self.titleDelay = MyGame.Manager.ConfigManager.ConfigData.TitleDelay
        self.flash = MyGame.Manager.ConfigManager.ConfigData.FlashTitle


    def LoadContent(self) -> None:
        super().LoadContent()

        self.globalCheat = MyGame.Manager.ConfigManager.ConfigData.CheatMode
        self.localCheat = self.globalCheat
        MyGame.Manager.QuestionManager.SetCheatMode(self.localCheat)

        MyGame.Manager.SoundManager.ResumeMusic()
        self.cheatCount = 0
        self.flag = False


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateTimer(deltaTime)
        if self.Timer > self.titleDelay:
            self.Timer = 0
            self.flag = not self.flag

        foward: bool = False
        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            # Check if hit Lisa head first then check cheat mode...
            cheatMode: bool = MyGame.Manager.InputManager.CheatMode()
            if cheatMode:
                if not self.localCheat:
                    self.cheatCount += 1
                    if self.cheatCount >= constants.NUMBER_CHEATS:
                        #  Tap Lisa head enough times to enable cheat!
                        self.localCheat = True
                        MyGame.Manager.QuestionManager.SetCheatMode(self.localCheat)
                        MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Cheat)
                else:
                    foward = MyGame.Manager.InputManager.Forward()
            else:
                foward = MyGame.Manager.InputManager.Forward()

        if foward:
            MyGame.Manager.SoundManager.PauseMusic()
            MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Right)
            super().BlockOnSoundFX()
            return enumerations.ScreenType.Diff

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        super().DrawScreenText()
        super().HideCheatMode()

        # Flash Press Start
        if not self.flash or not self.flag:
            return

        MyGame.Manager.SpriteManager.DrawWhite(self.whitePositions[0])
        MyGame.Manager.SpriteManager.DrawWhite(self.whitePositions[1])


    def __getTextPositions(self) -> list[pygame.Vector2]:
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 13))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 14))
        return positions


    def __getWhitePositions(self) -> list[pygame.Vector2]:
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetWhitePosition(2, 13))
        positions.append(MyGame.Manager.TextManager.GetWhitePosition(4, 13))
        return positions