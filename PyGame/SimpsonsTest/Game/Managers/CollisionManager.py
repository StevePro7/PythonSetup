import pygame
from Game.MyGame import MyGame
from Game.Static import Constants as const
from Game.Static import Enumerations as enums


class CollisionManager:

    def __init__(self):
        self.fullScreenRect: pygame.Rect = None
        self.volumeIconRect: pygame.Rect = None
        self.cheatModeRect: pygame.Rect = None
        self.optionRect: list[pygame.Rect] = None
        self.optionPos: list[pygame.Vector2] = None


    def LoadContent(self):
        self.fullScreenRect = pygame.Rect(0, 0, const.SCREEN_WIDE, const.SCREEN_HIGH)

        volumeIconPos: pygame.Vector2 = MyGame.Manager.BaseManager.GetVolumeIconPos()
        self.volumeIconRect = pygame.Rect(volumeIconPos.x, volumeIconPos.y, const.SpriteSize, const.SpriteSize)

        cheatModePos: pygame.Vector2 = MyGame.Manager.BaseManager.GetCheatModePos()
        self.cheatModeRect = pygame.Rect(cheatModePos.x, cheatModePos.y, const.SpriteSize, const.SpriteSize)

        characterPos: pygame.Vector2 = MyGame.Manager.BaseManager.GetCharacterPos()
        self.characterRect = pygame.Rect(characterPos.x, characterPos.y, const.imageWide, const.imageHigh)

        self.optionPos: list[pygame.Vector2] = MyGame.Manager.BaseManager.GetPositionsSelect()
        self.optionRect = [
            self.__getOptionRect(option_type)
            for option_type in enums.OptionType
            if option_type is not enums.OptionType.Invalid
        ]


    def FullScreen(self, x: int, y: int) -> bool:
        return self.fullScreenRect.collidepoint(x, y)


    def GetOptionType(self, x: int, y: int) -> enums.OptionType:
        for option_type in enums.OptionType:
            if option_type is enums.OptionType.Invalid:
                continue

            if self.optionRect[option_type.value].collidepoint(x, y):
                return option_type

        return enums.OptionType.Invalid


    def VolumeIcon(self, x: int, y: int) -> bool:
        return self.volumeIconRect.collidepoint(x, y)

    def CheatMode(self, x: int, y: int) -> bool:
        return self.cheatModeRect.collidepoint(x, y)

    def Character(self, x: int, y: int) -> bool:
        return self.characterRect.collidepoint(x, y)


    def __getOptionRect(self, type: enums.OptionType) -> pygame.Rect:
        # Shrink the collision.
        option: int = type.value
        offset: int = const.OffsetSelect
        collSize: int = const.SpriteSize - (2 * const.OffsetSelect)
        pos: pygame.Vector2 = self.optionPos[option]
        return pygame.Rect(pos.x + offset, pos.y + offset, collSize, collSize)
