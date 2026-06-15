from MyGame import MyGame
from Static.Assets import Assets
from Static.Colors import Colors
import constants as const
import enumerations as enums
import pygame


class SpriteManager:

    def __init__(self):
        self.positionsSelect: list[pygame.Vector2] = None
        self.positionsAnswer: list[pygame.Vector2] = None
        self.leftArrowPos: pygame.Vector2 = None
        self.rghtArrowPos: pygame.Vector2 = None
        self.volumePos: pygame.Vector2 = None
        self.offsetAnswerY: int = None


    def Initialize(self):
        self.offsetAnswerY = 18;        # only used once so place here


    def LoadContent(self):
        self.positionsSelect = MyGame.Manager.BaseManager.GetPositionsSelect()
        self.positionsAnswer: list[pygame.Vector2] = self.__getPositionsAnswer()
        self.volumePos = MyGame.Manager.BaseManager.GetVolumeIconPos()
        self.spriteRects: list[pygame.Rect] = self.__populateSpriteRects()


    def DrawSelectAll(self) -> None:
        self.DrawSelect(enums.OptionType.A)
        self.DrawSelect(enums.OptionType.B)
        self.DrawSelect(enums.OptionType.C)
        self.DrawSelect(enums.OptionType.D)

    def DrawSelect(self, optionType: enums.OptionType) -> None:
        position: pygame.Vector2 = self.positionsSelect[optionType.value]
        self.DrawSprite(enums.SpriteType.Select, position)

    def DrawRight(self, optionType: enums.OptionType) -> None:
        position: pygame.Vector2 = self.positionsAnswer[optionType.value]
        self.DrawWhite(position)
        self.DrawSprite(enums.SpriteType.Right, position)

    def DrawWrong(self, optionType: enums.OptionType) -> None:
        position: pygame.Vector2 = self.positionsAnswer[optionType.value]
        self.DrawWhite(position)
        self.DrawSprite(enums.SpriteType.Wrong, position)

    def DrawVolumeOn(self) -> None:
        self.DrawSprite(enums.SpriteType.VolumeOn, self.volumePos)

    def DrawVolumeOff(self) -> None:
        self.DrawSprite(enums.SpriteType.VolumeOff, self.volumePos)

    def DrawWhite(self, position: pygame.Vector2) -> None:
        self.DrawSprite(enums.SpriteType.White, position)

    def DrawSprite(self, spriteType: enums.SpriteType, position: pygame.Vector2) -> None:
        source_rect: pygame.Rect = self.spriteRects[spriteType.value]
        MyGame.Manager.GraphicsManager.DrawSprite(
            Assets.SpritesheetTexture, position, source_rect
        )


    def __getPositionsAnswer(self) -> list[pygame.Vector2]:
        y: int = 7
        positionsAnswer: list[pygame.Vector2] = []

        for index in range(len(enums.OptionType)):
            pos: pygame.Vector2 = self.__getPositionAnswer(0, y)
            positionsAnswer.append(pos)
            y += 4

        return positionsAnswer

    def __getPositionAnswer(self, x: int, y: int) -> pygame.Vector2:
        px: int = 2 + const.GameOffsetX + x * const.SpriteTile
        py: int = y * const.SpriteTile + self.offsetAnswerY
        return pygame.Vector2(px, py)


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