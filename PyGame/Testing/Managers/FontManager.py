import pygame
import constants as const
from Static.Assets import Assets
from MyGame import MyGame
import utils
from pathlib import Path

class FontManager:
    def __init__(self):
        self.color = None
        self.font: pygame.font.Font = None

    def Initialize(self):
        self.color: tuple = pygame.Color("white")


    def LoadContent(self):
        root: Path = utils.get_project_root()
        file: Path = root / "Fonts/emulogic.ttf"
        Assets.EmulogicFont = pygame.font.Font("Fonts/emulogic.ttf", const.FONT_SIZE)

    def Draw(self):
        MyGame.Manager.LogManager.Debug("MGR Draw")

