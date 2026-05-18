from MyGame import MyGame

class BarManager:

    def Initialize(self):
        MyGame.Manager.LogManager.Write("blah")
        print("BM steve Init")

    def LoadContent(self):
        print("BM steve Load #1")
        MyGame.Manager.FooManager.LoadContent()
        # old
        # foo: FooManager = ServiceRegistry.get(FooManager.__name__)
        # foo.LoadContent()

        print("BM steve Load #2")