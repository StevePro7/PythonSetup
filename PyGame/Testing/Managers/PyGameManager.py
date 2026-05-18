import pygame

class PyGameManager:
    def Initialize(self):
        pygame.init()

    def LoadContent(self):
        print("PyGameManager steve Load")

    def Update(self, gameTime):
        print(f"PyGameManager steve Update")

    def Draw(self):
        print("PyGameManager steve Draw")
