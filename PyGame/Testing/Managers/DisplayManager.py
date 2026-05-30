from MyGame import MyGame
import pygame

class DisplayManager:
    def __init__(self):
        self.screen: pygame.Surface = None
        self.size: tuple = None

    def Initialize(self):
        self.wide = MyGame.Manager.ConfigManager.ConfigData.Width
        self.high = MyGame.Manager.ConfigManager.ConfigData.Height
        self.size = (self.wide, self.high)

    def LoadContent(self):
        # MyGame.Manager.LogManager.Write("MGR Load")
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Hello World!!")

    def Clear(self, color: tuple=(0, 0, 0)):
        # MyGame.Manager.LogManager.Write("MGR Load")
        self.screen.fill(color)
        return

    def Present(self):
        pygame.display.flip()

    def Foo(self, surface):
        self.screen.blit(surface, (0, 0))
