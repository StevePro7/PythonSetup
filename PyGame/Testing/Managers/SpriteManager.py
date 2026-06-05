from MyGame import MyGame
from Static.Assets import Assets
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
        self.positionsSelect = MyGame.Manager.BaseManager.GetPositionsSelect()
        #self.positionsAnswer: list[pygame.Vector2] = None  # adriana
        self.leftArrowPos = MyGame.Manager.BaseManager.GetLeftArrowPos()
        self.rghtArrowPos = MyGame.Manager.BaseManager.GetRghtArrowPos()
        self.volumePos = MyGame.Manager.BaseManager.GetVolumeIconPos()


    def LoadContent(self):
        pass

    def Update(self, deltaTime: int):
        pass

    def Draw(self):
        pass

    def DrawSprite(self) -> None:
        pass
        # MyGame.Manager.GraphicsManager.DrawSprite(
        #     Assets.SpritesheetTexture,
        #     self.headPosn,
        #     self.headerRect,
        #     self.imageRotate)
