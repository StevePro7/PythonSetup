from MyGame import MyGame
from Objects.ConfigData import ConfigData
from pathlib import Path
from dataclasses import asdict
import constants as const
from enumerations import ScreenType
import tomllib
import utils


class ConfigManager:
    def Initialize(self):
        pass


    def LoadContent(self):
        root: Path = utils.get_project_root()
        file: Path = root / const.FILES_DIRECTORY / "config.toml"
        text = file.read_text()
        data = tomllib.loads(text)
        data[ScreenType.__name__] = ScreenType[data[ScreenType.__name__]]
        self.ConfigData = ConfigData(**data)


    def DumpConfig(self):
        msg: str = asdict(self.ConfigData)
        #print(msg) # adriana
        MyGame.Manager.LogManager.Debug(asdict(self.ConfigData))
