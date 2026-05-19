from MyGame import MyGame
from Objects.ConfigData import ConfigData
from pathlib import Path
from dataclasses import asdict
import tomllib



class ConfigManager:
    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")


    def LoadContent(self):
        path: str = "/home/stevepro/GitHub/StevePro7/PythonSetup/PyGame/Testing/Files/config.toml"
        file: Path = Path(path)
        text = file.read_text()
        data = tomllib.loads(text)
        self.ConfigData = ConfigData(**data)


    def DumpConfig(self):
        MyGame.Manager.LogManager.Write(asdict(self.ConfigData))
