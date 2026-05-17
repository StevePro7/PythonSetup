#from FooManager import FooManager


class BarManager:

    def Initialize(self):
        print("BM steve Init")

    def LoadContent(self):
        from MyGame import MyGame

        MyGame.Manager.FooManager.LoadContent()
        print("BM steve LoadContent")

    def Update(self):
        print(f"BM steve Update")

    def Draw(self):
        print("BM steve Draw")
