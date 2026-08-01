from pathlib import Path
from dataclasses import asdict
from Game.MyGame import MyGame
import tomllib

from Game.Objects.ConfigData import ConfigData
from Game.Static import Constants as const
from Game.Static.Enumerations import ScreenType, OptionType, DifficultyType


class ConfigManager:
    def __init__(self):
        self.contentRoot: Path = None
        self.configRoot: Path = None

    def Initialize(self):
        self.contentRoot = MyGame.Manager.BaseManager.GetContentRoot()
        self.configRoot = self.contentRoot / const.DATA_DIRECTORY / const.CONFIG_DIRECTORY


    def LoadContent(self):
        file: Path = self.configRoot / "GlobalConfig.toml"
        text = file.read_text()
        data: ConfigData = tomllib.loads(text)
        data[ScreenType.__name__] = ScreenType[data[ScreenType.__name__]]
        data[OptionType.__name__] = OptionType[data[OptionType.__name__]]
        data[DifficultyType.__name__] = DifficultyType[data[DifficultyType.__name__]]
        self.ConfigData = ConfigData(**data)


    def DumpConfig(self):
        MyGame.Manager.LogManager.Debug(asdict(self.ConfigData))
