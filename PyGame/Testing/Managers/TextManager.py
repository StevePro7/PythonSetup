from MyGame import MyGame
from Static.Assets import Assets
from Static.Colors import Colors

class TextManager:
    def Initialize(self):
        pass

    def LoadContent(self):
        pass

    def Update(self, deltaTime: int):
        pass

    def DrawText(self, text, position, color=Colors.White):
        MyGame.Manager.GraphicsManager.DrawText(Assets.EmulogicFont, text, position, color)
