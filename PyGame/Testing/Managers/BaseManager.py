import pygame
import constants as const
import enumerations as enums

class BaseManager:

    def GetNumberZO(self, number: int) -> str:
        return self.GetNumber(number, "0")

    def GetNumberSP(self, number: int) -> str:
        return self.GetNumber(number, " ")

    def GetNumber(self, number: int, paddingChar: str) -> str:
        return str(number).rjust(3, paddingChar)

    def GetPositionsSelect(self) -> list[pygame.Vector2]:
        y: int = 7
        positionsSelect: list[pygame.Vector2] = []

        for index in range(len(enums.OptionType)):
            pos: pygame.Vector2 = self.GetPositionSelect(0, y)
            positionsSelect.append(pos)
            y += 4

        return positionsSelect

    def GetPositionSelect(self, x: int, y: int) -> pygame.Vector2:
        px: int = const.GameOffsetX + x * const.SpriteTile + const.OffsetSelect
        py: int = y * const.SpriteTile + const.OffsetSelect
        return pygame.Vector2(px, py)

    # adriana
    # def GetLeftArrowPos(self) -> pygame.Vector2:
    #     arrowHigh: int = const.SCREEN_HIGH - const.SpriteSize + const.OffsetArrowY
    #     return pygame.Vector2(0, arrowHigh)
    #
    # def GetRghtArrowPos(self) -> pygame.Vector2:
    #     arrowHigh: int = const.SCREEN_HIGH - const.SpriteSize + const.OffsetArrowY
    #     return pygame.Vector2(const.SCREEN_WIDE - const.SpriteSize, arrowHigh)

    def GetVolumeIconPos(self) -> pygame.Vector2:
        x: int = const.SCREEN_WIDE - const.SpriteSize - const.GameOffsetX
        y: int = -const.FONT_SIZE / 2
        return pygame.Vector2(x, y)

    def GetCheatModePos(self) -> pygame.Vector2:
        x: int = const.CheatModeOffsetX + const.GameOffsetX
        y: int = const.CheatModeOffsetY
        return pygame.Vector2(x, y)

    def GetCharacterPos(self) -> pygame.Vector2:
        x: int = const.GameOffsetX + const.FONT_SIZE * const.FONT_SIZE
        y: int = const.NUMBER_SPRITES * const.FONT_SIZE
        return pygame.Vector2(x, y)
