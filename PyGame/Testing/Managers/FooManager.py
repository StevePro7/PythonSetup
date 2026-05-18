from MyGame import MyGame

class FooManager:
    def Initialize(self):
        #print("FooManager steve Init")
        MyGame.Manager.LogManager.Write("Foo MGR init")

    def LoadContent(self):
        print("FooManager steve Load")

    def Update(self, gameTime):
        print(f"FooManager steve Update")

    def Draw(self):
        print("FooManager steve Draw")
