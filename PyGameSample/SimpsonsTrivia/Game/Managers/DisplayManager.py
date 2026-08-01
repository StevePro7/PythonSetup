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
        self.screen: pygame.Surface = None          # Fullscreen display
        self.game_surface: pygame.Surface = None    # Fixed 640x480 surface
        self.size: tuple = None                     # Game resolution

        self.screen_size: tuple = None              # Fullscreen resolution
        self.scale: float = 1.0
        self.offset: tuple = (0, 0)


    def Initialize(self):
        self.size = (const.SCREEN_WIDE, const.SCREEN_HIGH)


    def LoadContent(self):
        full: bool = MyGame.Manager.ConfigManager.ConfigData.Fullscreen
        flag: int = 0
        if full:
            info = pygame.display.Info()
            self.screen_size = (info.current_w, info.current_h)
            flag = pygame.FULLSCREEN
        else:
            self.screen_size = (const.SCREEN_WIDE, const.SCREEN_HIGH)

        self.screen = pygame.display.set_mode(self.screen_size, flag)
        self.game_surface = pygame.Surface(self.size)

        pygame.display.set_caption(Globalize.SIMPSONS_TITLE)
        pygame.display.set_icon(Assets.IconTexture)

        self.scale = min(
            self.screen_size[0] / self.size[0],
            self.screen_size[1] / self.size[1]
        )

        scaled_width = int(self.size[0] * self.scale)
        scaled_height = int(self.size[1] * self.scale)

        offset_x = (self.screen_size[0] - scaled_width) // 2
        offset_y = (self.screen_size[1] - scaled_height) // 2
        self.offset = (offset_x, offset_y)

        MyGame.Manager.ResolutionManager.Configure(
            self.size,
            self.screen_size,
            self.scale,
            self.offset
        )


    def Clear(self, color: Colors.Black):
        self.game_surface.fill(color)


    def Present(self, color: Colors.Black):
        scaled_surface = pygame.transform.smoothscale(
            self.game_surface,
            (int(self.size[0] * self.scale), int(self.size[1] * self.scale))
        )

        self.screen.fill(color)

        self.screen.blit(scaled_surface, self.offset)
        pygame.display.flip()


    @property
    def Screen(self) -> pygame.Surface:
        return self.game_surface


    def _GetIcon(self, assetName: str) -> pygame.Surface:
        path: Path = MyGame.Manager.BaseManager.GetContentRoot()
        icon: Path = path / const.TEXTURES_DIRECTORY / assetName
        return icon
