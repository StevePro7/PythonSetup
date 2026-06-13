from MyGame import MyGame
import importlib
import pkgutil
import Screens
from Screens.BaseScreen import BaseScreen
from Static.Colors import Colors
from enumerations import ScreenType

ENGINE_SCREENS: str = "Screens"
ENGINE_SCREEN: str = "Screen"

class ScreenManager:

    def __init__(self):
        self.screens: dict = {}
        self.currScreen: ScreenType = ScreenType.Unknown
        self.nextScreen: ScreenType = ScreenType.Splash
        self.color = Colors.Black


    def Initialize(self):
        self._import_all_screens()
        screen_classes = self._build_screen_map()
        self.screens: dict[ScreenType, BaseScreen] = {
            st: cls()
            for st, cls in screen_classes.items()
        }
        for screen in self.screens.values():
            screen.Initialize()


    def LoadContent(self):
        self.nextScreen = MyGame.Manager.ConfigManager.ConfigData.ScreenType


    def Update(self, deltaTime: int):
        if self.currScreen != self.nextScreen:
            self.currScreen = self.nextScreen
            self.screens[self.currScreen].LoadContent()

            self.color = Colors.White
            if self.currScreen in (ScreenType.Splash, ScreenType.Unknown):
                self.color = Colors.Black

        tempScreen = self.screens[self.currScreen].Update(deltaTime)
        if tempScreen:
            self.nextScreen = tempScreen


    def Draw(self):
        MyGame.Manager.DisplayManager.Clear(self.color)
        self.screens[self.currScreen].Draw()
        MyGame.Manager.DisplayManager.Present()


    def _import_all_screens(self):
        for _, module_name, _ in pkgutil.iter_modules(Screens.__path__):
            if module_name == "BaseScreen":
                continue

            importlib.import_module(f"{ENGINE_SCREENS}.{module_name}")

    def _build_screen_map(self) -> dict[ScreenType, type[BaseScreen]]:
        screen_map: dict[ScreenType, type[BaseScreen]] = {}

        for screen_type in ScreenType:
            class_name = f"{screen_type.name}{ENGINE_SCREEN}"
            module = importlib.import_module(f"{ENGINE_SCREENS}.{class_name}")

            cls = getattr(module, class_name)
            screen_map[screen_type] = cls

        return screen_map

