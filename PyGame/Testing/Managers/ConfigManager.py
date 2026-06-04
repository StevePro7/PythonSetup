from MyGame import MyGame
from Objects.ConfigData import ConfigData
from pathlib import Path
from dataclasses import asdict
from enumerations import ScreenType
import tomllib
import utils


class ConfigManager:
    def Initialize(self):
        pass
        #MyGame.Manager.LogManager.Write("MGR init")


    def LoadContent(self):
        root: Path = utils.get_project_root()
        file: Path = root / "Files" / "config.toml"
        #path: str = "/home/stevepro/GitHub/StevePro7/PythonSetup/PyGame/Testing/Files/config.toml"
        #file: Path = Path(path)
        text = file.read_text()
        data = tomllib.loads(text)
        data[ScreenType.__name__] = ScreenType[data[ScreenType.__name__]]
        self.ConfigData = ConfigData(**data)
        #MyGame.Manager.LogManager.Write(f"start screen='{self.ConfigData.ScreenType.name}'")


    def DumpConfig(self):
        msg: str = asdict(self.ConfigData)
        print(msg)
        MyGame.Manager.LogManager.Debug(asdict(self.ConfigData))
