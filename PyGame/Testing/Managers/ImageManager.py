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
        self.currActor: const.NUMBER_CHARACTERS
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


    def DrawTitle(self) -> None:
        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            self.zeroPosn,
            self.titleRect,
            self.imageRotate)


    def DrawActor(self, index: int) -> None:
        actorPosn: pygame.Vector2 = self.actorVect.copy()
        actorRect: pygame.Rect = self.actorRects[index]
        # scale: float = 1.0
        #
        # if index == enums.ActorType.Lisa1.value or index == enums.ActorType.Lisa2.value:
        #     scale = 0.85
        #     actorPosn.y += 2 * const.FONT_SIZE

        MyGame.Manager.GraphicsManager.DrawTexture(
            Assets.SpritesheetTexture,
            actorPosn,
            actorRect)


    def __populateSpriteRects(self) -> list[pygame.Rect]:
        spriteRects: list[pygame.Rect] = []

        x: int = 4 * const.imageHigh - const.SpriteSize
        y: int = 2 * const.imageHigh

        for index in range(const.NUMBER_SPRITES):
            spriteRects.append(self.__getSpriteRect(x, y, index))

        return spriteRects

    def __populateActorRects(self) -> list[pygame.Rect]:

        x_coords = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
        y_coords = [2, 3, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

        actorRects: list[pygame.Rect] = []
        for x, y in zip(x_coords, y_coords):
            actorRects.append(self.__getActorRect(x, y))

        return actorRects


    def __getSpriteRect(self, x: int, y: int, index: int):
        ny = y + index * const.SpriteSize
        return pygame.Rect(x, ny, const.SpriteSize, const.SpriteSize)


    def __getActorRect(self, x: int, y: int) -> pygame.Rect:
        return pygame.Rect(x * const.imageWide, y * const.imageHigh, const.imageWide, const.imageHigh)