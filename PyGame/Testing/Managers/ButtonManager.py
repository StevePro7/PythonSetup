from MyGame import MyGame

class ButtonManager:
    def Initialize(self):
        MyGame.Manager.FooManager.LoadContent()
        print("ButtonManager steve Init")

    def LoadContent(self):
        print("ButtonManager steve Load")

    def Update(self, gameTime):
        print(f"ButtonManager steve Update")

    def Draw(self):
        print("ButtonManager steve Draw")
