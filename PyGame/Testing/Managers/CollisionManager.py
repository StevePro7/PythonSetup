from MyGame import MyGame
import constants as const
import enumerations as enums
import pygame

class CollisionManager:
    def __init__(self):
        self.fullScreenRect: pygame.Rect = None
        #self.leftArrowRect: pygame.Rect = None; self.rghtArrowRect: pygame.Rect = None
        self.volumeIconRect: pygame.Rect = None
        self.cheatModeRect: pygame.Rect = None
        self.optionRect: list[pygame.Rect] = None
        self.optionPos: list[pygame.Vector2] = None


    def LoadContent(self):
        self.fullScreenRect = pygame.Rect(0, 0, const.SCREEN_WIDE, const.SCREEN_HIGH)

        #Vector2 leftArrowPos = BaseData.GetLeftArrowPos();
        #Vector2 rghtArrowPos = BaseData.GetRghtArrowPos();

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


    def __getOptionRect(self, type: enums.OptionType) -> pygame.Rect:
        # Shrink the collision.
        option: int = type.value
        offset: int = const.OffsetSelect
        collSize: int = const.SpriteSize - (2 * const.OffsetSelect)
        pos: pygame.Vector2 = self.optionPos[option]
        return pygame.Rect(pos.x + offset, pos.y + offset, collSize, collSize)


