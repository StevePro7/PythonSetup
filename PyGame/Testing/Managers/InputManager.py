import pygame
from Inputs.KeyboardInput import KeyboardInput
from Inputs.MouseInput import MouseInput
#from JoystickInput


class InputManager:
    def __init__(self):
        self.keyboard: KeyboardInput = None
        self.mouse:MouseInput = None

    def Initialize(self):
        self.keyboard: KeyboardInput = KeyboardInput()
        self.mouse: MouseInput = MouseInput()


    def Update(self, deltaTime: int):
        self.keyboard.Update(deltaTime)
        self.mouse.Update(deltaTime)

    def Advance(self) -> bool:
        test = self.keyboard.KeyHold(pygame.K_SPACE)
        #test = self.keyboard.KeyPress(pygame.K_SPACE)
        return test