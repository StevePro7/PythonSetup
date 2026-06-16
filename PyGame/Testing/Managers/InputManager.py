import pygame

from MyGame import MyGame
from Inputs.KeyboardInput import KeyboardInput
from Inputs.MouseInput import MouseInput
import Static.Enumerations as enums


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


    # If press left mouse button OR right key OR space key then go forward.
    def Forward(self) -> bool:
        if self.mouse.ButtonHold(enums.MouseType.Left.value):
            return True

        return self.keyboard.KeyHold(pygame.K_RIGHT) or self.keyboard.KeyHold(pygame.K_SPACE)


    # If press right mouse button OR left key OR F12 key then go back.
    def Back(self) -> bool:
        if self.mouse.ButtonHold(enums.MouseType.Right.value):
            return True
        if self.keyboard.KeyHold(pygame.K_LEFT) or self.keyboard.KeyHold(pygame.K_F12):
            return True
        return False


    def FullScreen(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.FullScreen(self.mouse.CurrMouseX, self.mouse.CurrMouseY)


    def GetOptionType(self) -> enums.OptionType:
        if self.mouse.ButtonHold():
            return MyGame.Manager.CollisionManager.GetOptionType(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

        if self.keyboard.KeyHold(pygame.K_a) or self.keyboard.KeyHold(pygame.K_1) or self.keyboard.KeyHold(pygame.K_KP1):
            return enums.OptionType.A
        if self.keyboard.KeyHold(pygame.K_b) or self.keyboard.KeyHold(pygame.K_2) or self.keyboard.KeyHold(pygame.K_KP2):
            return enums.OptionType.B
        if self.keyboard.KeyHold(pygame.K_c) or self.keyboard.KeyHold(pygame.K_3) or self.keyboard.KeyHold(pygame.K_KP3):
            return enums.OptionType.C
        if self.keyboard.KeyHold(pygame.K_d) or self.keyboard.KeyHold(pygame.K_4) or self.keyboard.KeyHold(pygame.K_KP4):
            return enums.OptionType.D
        return enums.OptionType.Invalid


    def GetPosition(self) -> (int, int):
        return self.mouse.MousePosition()


    def VolumeIcon(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.VolumeIcon(self.mouse.CurrMouseX, self.mouse.CurrMouseY)


    def CheatMode(self) -> bool:
        if not self.mouse.ButtonHold():
            return False

        return MyGame.Manager.CollisionManager.CheatMode(self.mouse.CurrMouseX, self.mouse.CurrMouseY)


    # If click on Actor or press Return
    def Character(self) -> bool:
        if self.mouse.ButtonHold():
            return MyGame.Manager.CollisionManager.Character(self.mouse.CurrMouseX, self.mouse.CurrMouseY)

        if self.keyboard.KeyHold(pygame.K_RETURN):
            return True

        return False