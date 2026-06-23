import pygame
from Game.MyGame import MyGame
from Game.Static.Assets import Assets
from Game.Screens.BaseScreen import BaseScreen
from Game.Static import Enumerations as enums, Constants as const
from Game.Static.Enumerations import ScreenType


class SplashScreen(BaseScreen):

    def __init__(self):
        self.splashDelay: int = None
        self.position: pygame.Vector2 = None


    def Initialize(self) -> None:
        pass


    def LoadContent(self) -> None:
        super().LoadContent()
        self.splashDelay = MyGame.Manager.ConfigManager.ConfigData.SplashDelay
        wide: int = (const.SCREEN_WIDE - Assets.SplashTexture.get_width()) / 2
        high: int = (const.SCREEN_HIGH - Assets.SplashTexture.get_height()) / 2
        self.position: pygame.Vector2 = pygame.Vector2(wide, high)


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateTimer(deltaTime)
        if self.Timer > self.splashDelay:
            return enums.ScreenType.Init

        fullScreen: bool = MyGame.Manager.InputManager.FullScreen()
        if fullScreen:
            return enums.ScreenType.Init

        return None


    def Draw(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(Assets.SplashTexture, self.position)
