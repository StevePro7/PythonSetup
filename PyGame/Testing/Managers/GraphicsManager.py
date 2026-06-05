import pygame

from MyGame import MyGame
from Static.Colors import Colors

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


    # def DrawTexture(self, texture: pygame.Surface, position: pygame.Vector2):
    #     MyGame.Manager.DisplayManager.Screen.blit(texture, position)
    #
    def DrawTexture(
            self,
            texture: pygame.Surface,
            position: pygame.Vector2,
            source_rect: pygame.Rect | None = None,
            rotation: float = 0.0,
            scale: float = 1.0
    ):
        surface: pygame.Surface = texture

        if source_rect:
            surface = texture.subsurface(source_rect)

        if scale != 1.0:
            w: int = int(surface.get_width() * scale)
            h: int = int(surface.get_height() * scale)
            surface = pygame.transform.scale(surface, (w, h))

        if rotation:
            surface = pygame.transform.rotate(surface, rotation)

        MyGame.Manager.DisplayManager.Screen.blit(surface, position)


    def DrawText(self, font, text, position, color=Colors.White):
        surface = font.render(text, False, color)
        MyGame.Manager.DisplayManager.Screen.blit(surface, position)
