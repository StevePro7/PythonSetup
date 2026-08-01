import importlib
import pkgutil
import Game.Screens as Screens
from Game.MyGame import MyGame
from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Colors import Colors
from Game.Static.Enumerations import ScreenType
import Game.Static.Constants as const


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
        MyGame.Manager.DisplayManager.Present(self.color)


    def _import_all_screens(self):
        for _, module_name, _ in pkgutil.iter_modules(Screens.__path__):
            if module_name == BaseScreen.__name__:
                continue

            path_name: str = f"{const.GAME_DIRECTORY}.{ENGINE_SCREENS}.{module_name}"
            importlib.import_module(path_name)

    def _build_screen_map(self) -> dict[ScreenType, type[BaseScreen]]:
        screen_map: dict[ScreenType, type[BaseScreen]] = {}

        for screen_type in ScreenType:
            class_name = f"{screen_type.name}{ENGINE_SCREEN}"
            path_name: str = f"{const.GAME_DIRECTORY}.{ENGINE_SCREENS}.{class_name}"
            module = importlib.import_module(path_name)

            cls = getattr(module, class_name)
            screen_map[screen_type] = cls

        return screen_map
