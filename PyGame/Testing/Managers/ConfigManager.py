from MyGame import MyGame
from Objects.ConfigData import ConfigData
from pathlib import Path
from dataclasses import asdict
from enumerations import ScreenType
import tomllib



class ConfigManager:
    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")


    def LoadContent(self):
        base_dir = Path(__file__).resolve().parent.parent
        file: Path = base_dir / "Files" / "config.toml"
        #path: str = "/home/stevepro/GitHub/StevePro7/PythonSetup/PyGame/Testing/Files/config.toml"
        #file: Path = Path(path)
        text = file.read_text()
        data = tomllib.loads(text)
        data[ScreenType.__name__] = ScreenType[data[ScreenType.__name__]]
        self.ConfigData = ConfigData(**data)
        MyGame.Manager.LogManager.Write(f"start screen='{self.ConfigData.ScreenType.name}'")


    def DumpConfig(self):
        MyGame.Manager.LogManager.Write(asdict(self.ConfigData))
