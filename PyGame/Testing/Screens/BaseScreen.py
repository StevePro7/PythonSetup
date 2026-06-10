from abc import ABC, abstractmethod
import pygame
from enumerations import ScreenType
from Objects.TextData import TextData
from MyGame import MyGame


class BaseScreen(ABC):

    def __init__(self):
        self.Timer: int = None
        self.BuildPosition: pygame.Vector2 = None
        self.CheatPositions: list[pygame.Vector2] = None
        self.textDataList: list[TextData] = []


    @abstractmethod
    def Initialize(self) -> None:
        self.BuildPosition = self.__getBuildPosition()
        self.CheatPositions = self.__getCheatPositions()


    @abstractmethod
    def LoadContent(self) -> None:
        self.Timer = 0


    @abstractmethod
    def Update(self, deltaTime: int) -> ScreenType | None:
        return None

    @abstractmethod
    def Draw(self) -> None:
        pass


    def UpdateTimer(self, deltaTime: int):
        self.Timer += deltaTime

    def UpdateVolumeIcon(self) -> bool:
        volume: bool = MyGame.Manager.InputManager.VolumeIcon()
        if volume:
            MyGame.Manager.SoundManager.AlternateSound()

        return volume

    def InitScreenText(self) -> None:
        screen_name = self.__class__.__name__
        self.textDataList = MyGame.Manager.TextManager.InitTextData(screen_name)

    def DrawScreenText(self) -> None:
        MyGame.Manager.TextManager.DrawTextDataList(self.textDataList)

    def HideCheatMode(self) -> None:
        cheatMode: bool = MyGame.Manager.QuestionManager.GetCheatMode()
        if not cheatMode:
            MyGame.Manager.SpriteManager.DrawWhite(self.CheatPositions[0])
            MyGame.Manager.SpriteManager.DrawWhite(self.CheatPositions[1])

    def BlockOnSoundFX(self) -> None:
        while (MyGame.Manager.SoundManager.IsSoundPlaying()):
            pass

    def __getBuildPosition(self) -> pygame.Vector2:
        return MyGame.Manager.TextManager.GetTextPosition(26, 23)

    def __getCheatPositions(self) -> list[pygame.Vector2]:
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetTextPosition(25, 9))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(27, 9))
        return positions