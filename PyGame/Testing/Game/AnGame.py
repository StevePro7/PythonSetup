from Engine.Bootstrap import build_game
from Game.MyGame import MyGame

class AnGame:
    def __init__(self):
        self.running: bool = True
        build_game()


    def Initialize(self):
        MyGame.Initialize()


    def LoadContent(self):
        MyGame.LoadContent()


    def Update(self, deltaTime: int):
        MyGame.Update(deltaTime)


    def Draw(self):
        MyGame.Draw()


    def Exit(self):
        self.running = False


    def ShutDown(self):
        MyGame.ShutDown()


    def Run(self):
        self.Initialize()
        self.LoadContent()

        while self.running:
            MyGame.Manager.EventManager.ProcessEvents()
            if MyGame.Manager.EventManager.QuitRequested:
                self.Exit()

            deltaTime: int = MyGame.Manager.ClockManager.Update()
            self.Update(deltaTime)
            self.Draw()


