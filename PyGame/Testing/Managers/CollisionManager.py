from MyGame import MyGame
import constants as const
import enumerations as enums
import pygame

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

        # adriana - stream line
        self.optionPos: list[pygame.Vector2] = MyGame.Manager.BaseManager.GetPositionsSelect()
        self.optionRect = []
        self.optionRect.append(self.__getOptionRect(enums.OptionType.A))
        self.optionRect.append(self.__getOptionRect(enums.OptionType.B))
        self.optionRect.append(self.__getOptionRect(enums.OptionType.C))
        self.optionRect.append(self.__getOptionRect(enums.OptionType.D))


    def FullScreen(self, x: int, y: int) -> bool:
        return self.fullScreenRect.collidepoint(x, y)


    # adriana - stream line
    def GetOptionType(self, x: int, y: int) -> enums.OptionType:
        if self.optionRect[enums.OptionType.A.value].collidepoint(x, y):
            return enums.OptionType.A
        elif self.optionRect[enums.OptionType.B.value].collidepoint(x, y):
            return enums.OptionType.B
        elif self.optionRect[enums.OptionType.C.value].collidepoint(x, y):
            return enums.OptionType.C
        elif self.optionRect[enums.OptionType.D.value].collidepoint(x, y):
            return enums.OptionType.D

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


