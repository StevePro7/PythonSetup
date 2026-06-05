import pygame
import constants as const
import enumerations as enums
from Static.Assets import Assets
from MyGame import MyGame



class ImageManager:

    def __init__(self):
        self.currActor: int = None
        self.nextActor: int = None

    def Initialize(self):
        self.currActor = const.NUMBER_CHARACTERS
        self.nextActor = 0


    def LoadContent(self):
        self.zeroPosn: pygame.Vector2 = (const.GameOffsetX, 0)
        self.headPosn: pygame.Vector2 = (const.GameOffsetX, int(const.FONT_SIZE / 2))

        self.titleRect: pygame.Rect = pygame.Rect(0, 0, 2 * const.imageWide, 2 * const.imageHigh)
        self.titleVect: pygame.Vector2(const.imageWide * 2, 0)

        self.headerRect: pygame.Rect = pygame.Rect(4 * const.imageHigh - const.SpriteSize, 0, const.SpriteSize, 2 * const.imageHigh)
        self.headerVect: pygame.Vector2(const.SpriteSize, 0)

        self.actorRects: list[pygame.Rect] = self.__populateActorRects()
        self.actorVect: pygame.Vector2 = pygame.Vector2(const.SCREEN_WIDE - const.imageWide - const.GameOffsetX, const.SCREEN_HIGH - const.imageHigh)

        self.spriteRects: list[pygame.Rect] = self.__populateSpriteRects()
        self.imageRotate: float = 90   # degrees


    def GenerateNextActor(self):
        while True:
            self.nextActor: int = MyGame.Manager.RandomManager.Next(const.NUMBER_CHARACTERS)
            if self.currActor != self.nextActor:
                break

        self.currActor = self.nextActor


    def DrawTitle(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            self.zeroPosn,
            self.titleRect,
            self.imageRotate)


    def DrawHeader(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            self.headPosn,
            self.headerRect,
            self.imageRotate)

    def DrawCurrActor(self) -> None:
        self.DrawActor(self.currActor)


    def DrawActor(self, index: int) -> None:
        actorPosn: pygame.Vector2 = self.actorVect.copy()
        actorRect: pygame.Rect = self.actorRects[index]

        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            actorPosn,
            actorRect)

    @property
    def GetCurrActor(self):
        return self.currActor

    # Private methods
    def __populateActorRects(self) -> list[pygame.Rect]:

        x_coords = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
        y_coords = [2, 3, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

        actorRects: list[pygame.Rect] = []
        for x, y in zip(x_coords, y_coords):
            actorRects.append(self.__getActorRect(x, y))

        return actorRects

    def __getActorRect(self, x: int, y: int) -> pygame.Rect:
        return pygame.Rect(x * const.imageWide, y * const.imageHigh, const.imageWide, const.imageHigh)

    def __populateSpriteRects(self) -> list[pygame.Rect]:
        spriteRects: list[pygame.Rect] = []

        x: int = 4 * const.imageHigh - const.SpriteSize
        y: int = 2 * const.imageHigh

        for index in range(const.NUMBER_SPRITES):
            spriteRects.append(self.__getSpriteRect(x, y, index))

        return spriteRects

    def __getSpriteRect(self, x: int, y: int, index: int):
        ny = y + index * const.SpriteSize
        return pygame.Rect(x, ny, const.SpriteSize, const.SpriteSize)
