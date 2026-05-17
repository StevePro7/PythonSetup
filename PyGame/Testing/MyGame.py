from ServiceRegistry import ServiceRegistry


class MyGame:
    class _ManagerFacade:
        def __getattr__(self, name):
            return ServiceRegistry.get(name)

    Manager = _ManagerFacade()

    @staticmethod
    def Construct():
        print("MyGame Construct")

    @staticmethod
    def Initialize():
        MyGame.Manager.BarManager.Initialize()
        MyGame.Manager.FooManager.Initialize()
        print("Init complete")

    @staticmethod
    def LoadContent():
        MyGame.Manager.BarManager.LoadContent()
        MyGame.Manager.FooManager.LoadContent()


    @staticmethod
    def Update():
        pass