from Managers.BarManager import BarManager
from Managers.ImageManager import ImageManager
from Managers.CollisionManager import CollisionManager
from Managers.ScreenManager import ScreenManager
from Managers.QuestionManager import QuestionManager
from Managers.FooManager import FooManager
from Managers.SoundManager import SoundManager
from Managers.ScoreManager import ScoreManager
from Managers.InputManager import InputManager
from Managers.TextManager import TextManager
from Managers.DeviceManager import DeviceManager
from Managers.ButtonManager import ButtonManager
from Managers.ConfigManager import ConfigManager
from Managers.ThreadManager import ThreadManager
from Managers.StorageManager import StorageManager
from Managers.SpriteManager import SpriteManager
from Managers.ResolutionManager import ResolutionManager
from Managers.RandomManager import RandomManager
from Managers.ContentManager import ContentManager


class MyGame:
    @staticmethod
    def Construct(): ...

    @staticmethod
    def Initialize(): ...

    @staticmethod
    def LoadContent(): ...

    @staticmethod
    def Update(game_time: float): ...

    @staticmethod
    def Draw(): ...

    class Manager:
        ...
        BarManager: BarManager
        ImageManager: ImageManager
        CollisionManager: CollisionManager
        ScreenManager: ScreenManager
        QuestionManager: QuestionManager
        FooManager: FooManager
        SoundManager: SoundManager
        ScoreManager: ScoreManager
        InputManager: InputManager
        TextManager: TextManager
        DeviceManager: DeviceManager
        ButtonManager: ButtonManager
        ConfigManager: ConfigManager
        ThreadManager: ThreadManager
        StorageManager: StorageManager
        SpriteManager: SpriteManager
        ResolutionManager: ResolutionManager
        RandomManager: RandomManager
        ContentManager: ContentManager