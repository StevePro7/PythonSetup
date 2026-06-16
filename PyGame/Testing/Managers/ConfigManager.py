from pathlib import Path
from dataclasses import asdict
from MyGame import MyGame
import tomllib

from Objects.ConfigData import ConfigData
from Static import Constants as const
from Static.Enumerations import ScreenType, OptionType, DifficultyType


class ConfigManager:
    def Initialize(self):
        pass


    def LoadContent(self):
        root: Path = MyGame.Manager.BaseManager.GetProjectRoot()
        file: Path = root / const.CONFIG_DIRECTORY / "GlobalConfig.toml"
        text = file.read_text()
        data: ConfigData = tomllib.loads(text)
        data[ScreenType.__name__] = ScreenType[data[ScreenType.__name__]]
        data[OptionType.__name__] = OptionType[data[OptionType.__name__]]
        data[DifficultyType.__name__] = DifficultyType[data[DifficultyType.__name__]]
        self.ConfigData = ConfigData(**data)


    def DumpConfig(self):
        MyGame.Manager.LogManager.Debug(asdict(self.ConfigData))
