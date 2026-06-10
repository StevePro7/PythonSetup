import pygame

import enumerations
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


    def GetOptionType(self) -> enumerations.OptionType:
        if self.mouse.ButtonHold():
            return MyGame.Manager.CollisionManager.GetOptionType(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

        if self.keyboard.KeyHold(pygame.K_a) or self.keyboard.KeyHold(pygame.K_1) or self.keyboard.KeyHold(pygame.K_KP1):
            return enumerations.OptionType.A
        if self.keyboard.KeyHold(pygame.K_b) or self.keyboard.KeyHold(pygame.K_2) or self.keyboard.KeyHold(pygame.K_KP2):
            return enumerations.OptionType.B
        if self.keyboard.KeyHold(pygame.K_c) or self.keyboard.KeyHold(pygame.K_3) or self.keyboard.KeyHold(pygame.K_KP3):
            return enumerations.OptionType.C
        if self.keyboard.KeyHold(pygame.K_d) or self.keyboard.KeyHold(pygame.K_4) or self.keyboard.KeyHold(pygame.K_KP4):
            return enumerations.OptionType.D
        return enumerations.OptionType.Invalid


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