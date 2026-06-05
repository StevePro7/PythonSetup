import pygame
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Static.Assets import Assets
import constants as const
from enumerations import ScreenType

class SplashScreen(BaseScreen):

    def __init__(self):
        self.position: pygame.Vector2 = None


    def Initialize(self) -> None:
        pass


    def LoadContent(self) -> None:
        wide: int = (const.SCREEN_WIDE - Assets.SplashTexture.get_width()) / 2
        high: int = (const.SCREEN_HIGH - Assets.SplashTexture.get_height()) / 2
        self.position: pygame.Vector2 = pygame.Vector2(wide, high)


    def Update(self, deltaTime: int) -> ScreenType | None:
        #return ScreenType.Init
        return None


    def Draw(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(Assets.SplashTexture, self.position)
