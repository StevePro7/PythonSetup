from Engine.ServiceRegistry import ServiceRegistry


class MyGame:
    class _ManagerFacade:
        def __getattr__(self, name):
            return ServiceRegistry.get(name)

    Manager = _ManagerFacade()


    @staticmethod
    def Initialize():
        MyGame.Manager.PyGameManager.Initialize()
        MyGame.Manager.LogManager.Initialize()
        MyGame.Manager.BaseManager.Initialize()
        MyGame.Manager.RandomManager.Initialize()
        MyGame.Manager.TextManager.Initialize()

        MyGame.Manager.ConfigManager.Initialize()
        MyGame.Manager.ConfigManager.LoadContent()
        MyGame.Manager.ConfigManager.DumpConfig()

        MyGame.Manager.ClockManager.Initialize()
        MyGame.Manager.ContentManager.Initialize()

        MyGame.Manager.DisplayManager.Initialize()
        MyGame.Manager.ImageManager.Initialize()
        MyGame.Manager.InputManager.Initialize()
        MyGame.Manager.QuestionManager.Initialize()
        MyGame.Manager.ScoreManager.Initialize()
        MyGame.Manager.SpriteManager.Initialize()
        MyGame.Manager.ScreenManager.Initialize()
        MyGame.Manager.SoundManager.Initialize()



    @staticmethod
    def LoadContent():
        MyGame.Manager.CollisionManager.LoadContent()
        MyGame.Manager.ContentManager.LoadContent()
        MyGame.Manager.DisplayManager.LoadContent()

        MyGame.Manager.ImageManager.LoadContent()
        MyGame.Manager.QuestionManager.LoadContent()
        MyGame.Manager.ScoreManager.LoadContent()
        MyGame.Manager.SpriteManager.LoadContent()
        MyGame.Manager.ScreenManager.LoadContent()
        MyGame.Manager.SoundManager.LoadContent()


    @staticmethod
    def Update(deltaTime: int):
        MyGame.Manager.InputManager.Update(deltaTime)
        MyGame.Manager.ScreenManager.Update(deltaTime)


    @staticmethod
    def Draw():
        MyGame.Manager.ScreenManager.Draw()


    @staticmethod
    def ShutDown():
        MyGame.Manager.PyGameManager.Quit()
