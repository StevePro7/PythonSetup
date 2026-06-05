import pygame
from pathlib import Path

from MyGame import MyGame
from Static.Assets import Assets
import constants as const
import utils


class ContentManager:
    def __init__(self):
        self.contentRoot: Path = None
        self.texturesRoot: Path = None


    def Initialize(self):
        self.contentRoot: Path = utils.get_project_root()
        self.texturesRoot: Path = self.contentRoot / const.TEXTURES_DIRECTORY


    def LoadContent(self):
        # Load font
        file: Path = self.contentRoot / const.FONTS_DIRECTORY / "emulogic.ttf"
        Assets.EmulogicFont = pygame.font.Font(file, const.FONT_SIZE)

        # Load images
        Assets.SplashTexture: pygame.Surface = self._LoadTexture("Splash.bmp")
        Assets.SplashTexture: pygame.Surface = self._LoadTexture("StevePro.bmp")   # adriana
        Assets.SpritesheetTexture: pygame.Surface = self._LoadTexture("Spritesheet.png")


    # adriana
    def Update(self, deltaTime: int):
        pass

    # adriana
    def Draw(self):
        pass


    def _LoadTexture(self, assetName: str) -> pygame.Surface:
        path: Path = self.contentRoot / const.TEXTURES_DIRECTORY
        file: Path = path  / assetName
        texture = pygame.image.load(file).convert_alpha()
        return texture