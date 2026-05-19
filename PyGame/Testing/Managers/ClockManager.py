from MyGame import MyGame

class ClockManager:
    def Initialize(self):
        #print("ClockManager steve Init")
        MyGame.Manager.LogManager.Write("Foo MGR init")

    def LoadContent(self):
        print("ClockManager steve Load")

    def Update(self, gameTime):
        print(f"ClockManager steve Update")

    def Draw(self):
        print("ClockManager steve Draw")
