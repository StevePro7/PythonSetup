from bootstrap import build_game
from MyGame import MyGame

class AnGame:
    def __init__(self):
        self.running: bool = True
        build_game()


    def Initialize(self):
        MyGame.Initialize()


    def LoadContent(self):
        MyGame.LoadContent()

    def Update(self):
        MyGame.Update()

    def Draw(self):
        MyGame.Draw()

    def Exit(self):
        self.running = True


    def Run(self):
        self.Initialize()
        self.LoadContent()

        while self.running:
            self.Update()
            MyGame.Manager.LogManager.Write("ddd")
            self.Draw()




