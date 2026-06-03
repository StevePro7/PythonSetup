import pygame
import constants as const
from Static.Assets import Assets
from MyGame import MyGame
import utils
from pathlib import Path


class ImageManager:

    def __init__(self):
        self.currActor: int = None
        self.nextActor: int = None

    def Initialize(self):
        self.currActor: const.NUMBER_CHARACTERS
        self.nextActor = 0

    def LoadContent(self):
        root: Path = utils.get_project_root()
        file: Path = root / "Spritesheet.png"
        #Assets.SpritesheetTexture = pygame.image.load(file).convert_alpha()        # adriana - move to Content MGR

        self.zeroPosn: pygame.Vector2 = (const.GameOffsetX, 0)
        self.headPosn: pygame.Vector2 = (const.GameOffsetX, int(const.FONT_SIZE / 2))

        self.titleRect: pygame.Rect = pygame.Rect(0, 0, 2 * const.imageWide, 2 * const.imageHigh)
        self.titleVect: pygame.Vector2(const.imageWide * 2, 0)

        self.headerRect: pygame.Rect = pygame.Rect(4 * const.imageHigh - const.SpriteSize, 0, const.SpriteSize, 2 * const.imageHigh)
        self.headerVect: pygame.Vector2(const.SpriteSize, 0)

        self.actorRects: list[pygame.Rect] = self.__populateActorRects()
        print("eee")


    def __populateActorRects(self) -> list[pygame.Rect]:

        x_coords = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
        y_coords = [2, 3, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

        actorRects: list[pygame.Rect] = []
        for x, y in zip(x_coords, y_coords):
            actorRects.append(self.__getActorRect(x, y))

        return actorRects


    def __getActorRect(self, x: int, y: int) -> pygame.Rect:
        return pygame.Rect(x * const.imageWide, y * const.imageHigh, const.imageWide, const.imageHigh)