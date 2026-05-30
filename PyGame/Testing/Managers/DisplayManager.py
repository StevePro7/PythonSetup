from MyGame import MyGame
from Static.Globalize import Globalize
import pygame

# Window ownership
class DisplayManager:
    def __init__(self):
        self.screen: pygame.Surface = None
        self.size: tuple = None

    def Initialize(self):
        wide = MyGame.Manager.ConfigManager.ConfigData.Width
        high = MyGame.Manager.ConfigManager.ConfigData.Height
        self.size = (wide, high)

    def LoadContent(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(Globalize.SIMPSONS_TITLE)

    def Clear(self, color: tuple=(0, 0, 0)):
        self.screen.fill(color)

    def Present(self):
        pygame.display.flip()

    @property
    def Screen(self) -> pygame.Surface:
        return self.screen
