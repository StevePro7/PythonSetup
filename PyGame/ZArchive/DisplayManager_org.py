import pygame
from pathlib import Path

from Game.MyGame import MyGame
from Game.Static.Assets import Assets
from Game.Static.Colors import Colors
from Game.Static.Globalize import Globalize
from Game.Static import Constants as const


# Window ownership
class DisplayManager:

    def __init__(self):
        self.screen: pygame.Surface = None
        self.size: tuple = None


    def Initialize(self):
        self.size = (const.SCREEN_WIDE, const.SCREEN_HIGH)


    def LoadContent(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(Globalize.SIMPSONS_TITLE)
        pygame.display.set_icon(Assets.IconTexture)


    def Clear(self, color: Colors.Black):
        self.screen.fill(color)


    def Present(self):
        pygame.display.flip()


    @property
    def Screen(self) -> pygame.Surface:
        return self.screen


    def _GetIcon(self, assetName: str) -> pygame.Surface:
        path: Path = MyGame.Manager.BaseManager.GetContentRoot()
        icon: Path = path / const.TEXTURES_DIRECTORY / assetName
        return icon