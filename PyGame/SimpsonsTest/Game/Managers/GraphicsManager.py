import pygame
from Game.MyGame import MyGame
from Game.Static.Colors import Colors


# Rendering API.
class GraphicsManager:

    def Initialize(self):
        pass

    def LoadContent(self):
        pass


    def Update(self, deltaTime: int):
        pass


    def DrawSprite(
            self,
            texture: pygame.Surface,
            position: pygame.Vector2,
            source_rect: pygame.Rect | None = None
    ):
        surface: pygame.Surface = texture

        if source_rect:
            surface = texture.subsurface(source_rect)

        MyGame.Manager.DisplayManager.Screen.blit(surface, position)


    def DrawTexture(
            self,
            texture: pygame.Surface,
            position: pygame.Vector2,
            source_rect: pygame.Rect | None = None,
            rotation: float = 0.0
    ):
        surface: pygame.Surface = texture

        if source_rect:
            surface = texture.subsurface(source_rect)

        if rotation:
            surface = pygame.transform.rotate(surface, rotation)

        MyGame.Manager.DisplayManager.Screen.blit(surface, position)


    def DrawText(self, font, text, position, color=Colors.White):
        surface = font.render(text, False, color)
        MyGame.Manager.DisplayManager.Screen.blit(surface, position)
