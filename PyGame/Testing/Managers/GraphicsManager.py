from MyGame import MyGame
from Static.Assets import Assets

# Rendering API
class GraphicsManager:
    def Initialize(self):
        pass

    def LoadContent(self):
        return None

    def Update(self, deltaTime: int):
        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")


    def DrawText(self, font, text, position, color=(255,255,255)):
        surface = font.render(text, False, color)
        MyGame.Manager.DisplayManager.Screen.blit(surface, position)
        pass