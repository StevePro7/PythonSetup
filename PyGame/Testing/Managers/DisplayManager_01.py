import pygame
from pathlib import Path

from MyGame import MyGame
from Static.Assets import Assets
from Static.Colors import Colors
from Static.Globalize import Globalize
import constants as const
#import enumerations as enums

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


    def Clear(self, color: Colors.Black):
        self.game_surface.fill(color)


    def Present(self):
        scaled_surface = pygame.transform.scale(
            self.game_surface,
            (int(self.size[0] * self.scale), int(self.size[1] * self.scale))
        )

        self.screen.fill((0, 0, 0))

        self.screen.blit(scaled_surface, self.offset)
        pygame.display.flip()


    @property
    def Screen(self) -> pygame.Surface:
        return self.game_surface


    def _GetIcon(self, assetName: str) -> pygame.Surface:
        path: Path = MyGame.Manager.BaseManager.GetContentRoot()
        icon: Path = path / const.TEXTURES_DIRECTORY / assetName
        return icon

    def GetMousePosition(self) -> tuple:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Remove offset (center position)
        x = mouse_x - self.offset[0]
        y = mouse_y - self.offset[1]

        # If outside the game area, ignore
        if x < 0 or y < 0:
            return (-1, -1)

        max_w = int(self.size[0] * self.scale)
        max_h = int(self.size[1] * self.scale)

        if x > max_w or y > max_h:
            return (-1, -1)

        # Convert back to 640x480 space
        x = int(x / self.scale)
        y = int(y / self.scale)

        return (x, y)
