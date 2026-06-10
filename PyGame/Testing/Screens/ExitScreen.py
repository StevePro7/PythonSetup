import pygame

from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType
from enumerations import SpriteType, OptionType


class ExitScreen(BaseScreen):

    def Initialize(self) -> None:
        self.actor = 0
        self.voice = str(self.actor)


    def LoadContent(self) -> None:
        MyGame.Manager.ImageManager.GenerateNextActor()
        self.actor = MyGame.Manager.ImageManager.GetCurrActor
        self.voice = str(self.actor)


    def Update(self, deltaTime: int) -> ScreenType | None:
        type: OptionType = MyGame.Manager.InputManager.GetOptionType()
        if type != OptionType.Invalid:
            print(type.value)

        back: bool = MyGame.Manager.InputManager.Back()
        if back:
            print("Go BACK")

        forward: bool = MyGame.Manager.InputManager.Forward()
        if forward:
            print("go forward")
        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawHeader()
        MyGame.Manager.ImageManager.DrawCurrActor()
        #MyGame.Manager.ImageManager.DrawActor(self.actor)
        pos: pygame.Vector2 = (50, 50)
        MyGame.Manager.SpriteManager.DrawSprite(SpriteType.Select, pos)
        MyGame.Manager.TextManager.DrawText(str(self.voice), 0, 0)
        pass
