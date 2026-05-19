from MyGame import MyGame
from Objects.ConfigData import ConfigData
from pathlib import Path

class ConfigManager:
    def Initialize(self):
        MyGame.Manager.LogManager.Write("MGR init")
        self.ConfigData = ConfigData()

    def LoadContent(self):
        path: str = "/home/stevepro/GitHub/StevePro7/PythonSetup/PyGame/Testing/Files/config.txt"
        file_path: Path = Path(path)
        values: dict = {}

        for line in file_path.read_text().splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()

        self.ConfigData = ConfigData(
            FPS=int(values.get("FPS")),
            Width=values.get("Width"),
        )