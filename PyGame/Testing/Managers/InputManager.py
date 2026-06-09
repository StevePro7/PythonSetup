import pygame

from MyGame import MyGame
from Inputs.KeyboardInput import KeyboardInput
from Inputs.MouseInput import MouseInput
#from JoystickInput


class InputManager:
    def __init__(self):
        self.keyboard: KeyboardInput = None
        self.mouse: MouseInput = None

    def Initialize(self):
        self.keyboard: KeyboardInput = KeyboardInput()
        self.mouse: MouseInput = MouseInput()


    def Update(self, deltaTime: int):
        self.keyboard.Update(deltaTime)
        self.mouse.Update(deltaTime)


    def Advance(self) -> bool:
        if self.mouse.ButtonClick():
            return True

        return self.keyboard.KeyHold(pygame.K_SPACE)


    def FullScreen(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.FullScreen(self.mouse.CurrMouseX, self.mouse.CurrMouseY)


    def GetOptionType(self) -> bool:
        test = self.mouse.ButtonClick()
        return test

    def GetPosition(self) -> (int, int):
        return self.mouse.MousePosition()

    # public Boolean LeftArrow()
    # public Boolean RghtArrow()

    def VolumeIcon(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.VolumeIcon(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

    def CheatMode(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.CheatMode(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

    def Character(self) -> bool:
        if self.mouse.ButtonHold():
            return MyGame.Manager.CollisionManager.Character(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

        if self.keyboard.KeyHold(pygame.K_RIGHT):
            return True

        return False