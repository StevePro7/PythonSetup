from MyGame import MyGame
import pygame

class ContentManager:
    def __init__(self):
        self.font: pygame.font.Font = None

    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")

    def LoadContent(self):
        font_size: int = 20
        self.font = pygame.font.Font("Fonts/emulogic.ttf", font_size)

        self.wide = MyGame.Manager.ConfigManager.ConfigData.Width
        self.high = MyGame.Manager.ConfigManager.ConfigData.Height
        self.screen = pygame.display.set_mode((self.wide, self.high))
        pygame.display.set_caption("Hello World")

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")

    def Draw(self):
        pygame.display.flip()
