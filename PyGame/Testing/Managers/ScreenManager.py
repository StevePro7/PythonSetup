from MyGame import MyGame
import importlib
import pkgutil
import Screens
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType

class ScreenManager:

    def __init__(self):
        self.screens: dict = {}
        self.currScreen: ScreenType = ScreenType.Splash
        self.nextScreen: ScreenType = ScreenType.Splash

    def Initialize(self):
        import_all_screens()
        screen_classes = build_screen_map()
        self.screens: dict[ScreenType, BaseScreen] = {
            st: cls()
            for st, cls in screen_classes.items()
        }

    #    self.currScreen: ScreenType = ScreenType.Splash
    #    self.nextScreen: ScreenType = ScreenType.Splash



    def LoadContent(self):
        MyGame.Manager.LogManager.Write("MGR Load")

    def Update(self, deltaTime: int):
        if self.currScreen != self.nextScreen:
            self.currScreen = self.nextScreen
            self.screens[self.currScreen].LoadContent()

        tempScreen = self.screens[self.currScreen].Update(deltaTime)
        if tempScreen:
            self.nextScreen = tempScreen

        MyGame.Manager.LogManager.Write(f"MGR Update({deltaTime})")


    def Draw(self):
        self.screens[self.currScreen].Draw()
        MyGame.Manager.LogManager.Write("MGR Draw")


def import_all_screens():
    for _, module_name, _ in pkgutil.iter_modules(Screens.__path__):
        if module_name == "BaseScreen":
            continue

        importlib.import_module(f"Screens.{module_name}")


def build_screen_map() -> dict[ScreenType, type[BaseScreen]]:
    screen_map = {}

    for screen_type in ScreenType:
        class_name = f"{screen_type.name}Screen"
        module = importlib.import_module(f"Screens.{class_name}")

        cls = getattr(module, class_name)

        screen_map[screen_type] = cls

    return screen_map