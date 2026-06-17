import pygame
from Game.MyGame import MyGame
from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Enumerations import ScreenType
from Game.Static.Enumerations import SpriteType
from Game.Static import Enumerations as enums


class ExitScreen(BaseScreen):

    def Initialize(self) -> None:
        self.actor = 0
        self.voice = str(self.actor)


    def LoadContent(self) -> None:
        MyGame.Manager.ImageManager.GenerateNextActor()
        self.actor = MyGame.Manager.ImageManager.GetCurrActor
        self.voice = str(self.actor)


    def Update(self, deltaTime: int) -> ScreenType | None:
        full: bool = MyGame.Manager.InputManager.FullScreen()
        if full:
            val = MyGame.Manager.RandomManager.Next(3)
            val += 4
            print(val)
            sfx = enums.SoundType(val)
            MyGame.Manager.SoundManager.PlaySound(sfx)

        # stop: bool = MyGame.Manager.InputManager.VolumeIcon()
        # if stop:
        #     MyGame.Manager.SoundManager.StopMusic()
        #     print("stop")
        #
        # back: bool = MyGame.Manager.InputManager.Back()
        # if back:
        #     MyGame.Manager.SoundManager.PauseMusic()
        #     print("pause")
        #
        # forward: bool = MyGame.Manager.InputManager.Forward()
        # if forward:
        #     MyGame.Manager.SoundManager.ResumeMusic()
        #     print("resume")

        return None


    # def Update(self, deltaTime: int) -> ScreenType | None:
    #     type: OptionType = MyGame.Manager.InputManager.GetOptionType()
    #     if type != OptionType.Invalid:
    #         print(type.value)
    #
    #     back: bool = MyGame.Manager.InputManager.Back()
    #     if back:
    #         print("Go BACK")
    #
    #     forward: bool = MyGame.Manager.InputManager.Forward()
    #     if forward:
    #         print("go forward")
    #
    #     return None

    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawHeader()
        MyGame.Manager.ImageManager.DrawCurrActor()
        #MyGame.Manager.ImageManager.DrawActor(self.actor)
        pos: pygame.Vector2 = (50, 50)
        MyGame.Manager.SpriteManager.DrawSprite(SpriteType.Select, pos)
        MyGame.Manager.TextManager.DrawText(str(self.voice), 0, 0)
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        pass
