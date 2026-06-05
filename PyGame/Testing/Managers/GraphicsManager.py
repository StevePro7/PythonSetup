import pygame

from MyGame import MyGame
from Static.Assets import Assets

# Rendering API
class GraphicsManager:
    def Initialize(self):
        pass

    def LoadContent(self):
        pass
        #return None

    def Update(self, deltaTime: int):
        pass
#        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")


    def DrawTexture(self, texture: pygame.Surface, position: pygame.Vector2):
        MyGame.Manager.DisplayManager.Screen.blit(texture, position)

    def DrawText(self, font, text, position, color=(255,255,255)):
        surface = font.render(text, False, color)
        MyGame.Manager.DisplayManager.Screen.blit(surface, position)
