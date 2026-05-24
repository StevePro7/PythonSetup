from ServiceRegistry import ServiceRegistry


class MyGame:
    class _ManagerFacade:
        def __getattr__(self, name):
            return ServiceRegistry.get(name)

    Manager = _ManagerFacade()


    @staticmethod
    def Initialize():
        MyGame.Manager.PyGameManager.Initialize()
        MyGame.Manager.LogManager.Initialize()
        MyGame.Manager.ConfigManager.Initialize()
        MyGame.Manager.ConfigManager.LoadContent()
        MyGame.Manager.ConfigManager.DumpConfig()

        MyGame.Manager.ClockManager.Initialize()
        MyGame.Manager.ScreenManager.Initialize()
        # MyGame.Manager.FooManager.Initialize()
        # MyGame.Manager.ButtonManager.Initialize()
        MyGame.Manager.LogManager.Write("Init complete")


    @staticmethod
    def LoadContent():
        MyGame.Manager.ContentManager.LoadContent()
        MyGame.Manager.ScreenManager.LoadContent()
        pass


    @staticmethod
    def Update(deltaTime: int):
        MyGame.Manager.LogManager.Write(f"DT={deltaTime}")
        MyGame.Manager.ScreenManager.Update(deltaTime)

    @staticmethod
    def Draw():
        MyGame.Manager.ScreenManager.Draw()
