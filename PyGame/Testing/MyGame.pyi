from Managers.BaseManager import BaseManager
from Managers.ClockManager import ClockManager
from Managers.CollisionManager import CollisionManager
from Managers.ConfigManager import ConfigManager
from Managers.ContentManager import ContentManager
from Managers.DebugManager import DebugManager
from Managers.DisplayManager import DisplayManager
from Managers.EventManager import EventManager
from Managers.FileManager import FileManager
from Managers.FontManager import FontManager
from Managers.FooManager import FooManager
from Managers.GraphicsManager import GraphicsManager
from Managers.ImageManager import ImageManager
from Managers.InputManager import InputManager
from Managers.LogManager import LogManager
from Managers.PyGameManager import PyGameManager
from Managers.QuestionManager import QuestionManager
from Managers.RandomManager import RandomManager
from Managers.ResolutionManager import ResolutionManager
from Managers.ScoreManager import ScoreManager
from Managers.ScreenManager import ScreenManager
from Managers.SoundManager import SoundManager
from Managers.SpriteManager import SpriteManager
from Managers.StorageManager import StorageManager
from Managers.TextManager import TextManager
from Managers.ThreadManager import ThreadManager


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
        BaseManager: BaseManager
        ClockManager: ClockManager
        CollisionManager: CollisionManager
        ConfigManager: ConfigManager
        ContentManager: ContentManager
        DebugManager: DebugManager
        DisplayManager: DisplayManager
        EventManager: EventManager
        FileManager: FileManager
        FontManager: FontManager
        FooManager: FooManager
        GraphicsManager: GraphicsManager
        ImageManager: ImageManager
        InputManager: InputManager
        LogManager: LogManager
        PyGameManager: PyGameManager
        QuestionManager: QuestionManager
        RandomManager: RandomManager
        ResolutionManager: ResolutionManager
        ScoreManager: ScoreManager
        ScreenManager: ScreenManager
        SoundManager: SoundManager
        SpriteManager: SpriteManager
        StorageManager: StorageManager
        TextManager: TextManager
        ThreadManager: ThreadManager