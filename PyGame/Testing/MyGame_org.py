from ServiceRegistry import ServiceRegistry


class _ManagerFacade:
    """
    Enables:
        MyGame.Manager.FooManager
    """
    def __getattr__(self, name):
        return ServiceRegistry.get(name)


class MyGame:
    # class _ManagerFacade:
    #     def __getattr__(self, name):
    #         return ServiceRegistry.get(name)

    Manager = _ManagerFacade()

    @staticmethod
    def Construct():
        print("MyGame Construct")

    @staticmethod
    def Initialize():
        MyGame.Manager.FooManager.Initialize()
        MyGame.Manager.BarManager.Initialize()
        print("Init complete")

    @staticmethod
    def LoadContent():
        MyGame.Manager.FooManager.LoadContent()
        MyGame.Manager.BarManager.LoadContent()