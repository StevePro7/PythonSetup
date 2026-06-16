import pygame

import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Static.Assets import Assets
from Static import Constants as const
from enumerations import ScreenType

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
            return enumerations.ScreenType.Init

        fullScreen: bool = MyGame.Manager.InputManager.FullScreen()
        if fullScreen:
            return enumerations.ScreenType.Init

        return None


    def Draw(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(Assets.SplashTexture, self.position)
