from MyGame import MyGame

class BaseScreen:
    def Initialize(self):
        print("BaseScreen steve Init")

    def LoadContent(self):
        print("BaseScreen steve Load")

    def Update(self, gameTime):
        print(f"BaseScreen steve Update")

    def Draw(self):
        print("BaseScreen steve Draw")