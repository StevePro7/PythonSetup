import pygame
from pathlib import Path

from MyGame import MyGame
from Static.Assets import Assets
from Static import Constants as const


class ContentManager:
    def __init__(self):
        self.contentRoot: Path = None
        self.texturesRoot: Path = None


    def Initialize(self):
        self.contentRoot = MyGame.Manager.BaseManager.GetContentRoot()
        self.texturesRoot = self.contentRoot / const.TEXTURES_DIRECTORY


    def LoadContent(self):
        # Load font
        file: Path = self.contentRoot / const.FONTS_DIRECTORY / "emulogic.ttf"
        Assets.EmulogicFont = pygame.font.Font(file, const.FONT_SIZE)

        # Load images
        Assets.SplashTexture: pygame.Surface = self._LoadTexture("StevePro.bmp")
        Assets.SpritesheetTexture: pygame.Surface = self._LoadTexture("Spritesheet.png")
        Assets.IconTexture: pygame.Surface = self._LoadTexture("DonutIcon.png")


    def _LoadTexture(self, assetName: str) -> pygame.Surface:
        file: Path = self.texturesRoot / assetName
        texture = pygame.image.load(file)
        return texture
