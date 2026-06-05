import pygame

from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType
from enumerations import SpriteType


class ExitScreen(BaseScreen):

    def Initialize(self) -> None:
        self.actor = 0
        self.voice = str(self.actor)


    def LoadContent(self) -> None:
        MyGame.Manager.ImageManager.GenerateNextActor()
        self.actor = MyGame.Manager.ImageManager.GetCurrActor
        self.voice = str(self.actor)


    def Update(self, deltaTime: int) -> ScreenType | None:
        # test: bool = MyGame.Manager.InputManager.Advance()
        # if test:
        #     self.actor += 1
        #     self.voice = str(self.actor)

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawHeader()
        MyGame.Manager.ImageManager.DrawCurrActor()
        #MyGame.Manager.ImageManager.DrawActor(self.actor)
        pos: pygame.Vector2 = (50, 50)
        MyGame.Manager.SpriteManager.DrawSprite(SpriteType.Select, pos)
        MyGame.Manager.TextManager.DrawText(str(self.voice), 0, 0)
        pass
