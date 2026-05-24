from MyGame import MyGame
import pygame

class ContentManager:
    def __init__(self):
        self.font: pygame.font.Font = None

    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")

    def LoadContent(self):
        self.font_size: int = 20
        self.font = pygame.font.Font("Fonts/emulogic.ttf", self.font_size)

        self.wide = MyGame.Manager.ConfigManager.ConfigData.Width
        self.high = MyGame.Manager.ConfigManager.ConfigData.Height
        self.size = (self.wide, self.high)
        self.screen = pygame.display.set_mode(self.size)
        self.writer = pygame.Surface(self.size)

        #self.text = self.font.render("X", False, (255, 255, 255))
        pygame.display.set_caption("Hello World")

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")

    def Draw(self):
        self.writer.fill((0, 0, 0))

        # for x in range(32):
        #     for y in range(24):
        #         coord: tuple = (x * self.font_size, y * self.font_size)
        #         z = x % 10
        #         t = str(z)
        #         text = self.font.render(t, False, (255, 255, 255))
        #         self.writer.blit(text, coord)

        for x in range(32):
            coord: tuple = (x * self.font_size, 0)
            z = x % 10
            t = str(z)
            text = self.font.render(t, False, (255, 255, 255))
            self.writer.blit(text, coord)

        # for y in range(24):
        #     coord: tuple = (0, y * self.font_size)
        #     z = y % 10
        #     t = str(z)
        #     text = self.font.render(t, False, (255, 255, 255))
        #     self.writer.blit(text, coord)

        scaled = pygame.transform.scale(self.writer, self.size)
        self.screen.blit(scaled, (0, 0))

        pygame.display.flip()
