from Managers.FileManager import FileManager
from MyGame import MyGame
from bootstrap import build_game
from pathlib import Path

registry = build_game()

fileManager = registry.get(FileManager.__name__)
root: Path = MyGame.Manager.BaseManager.GetProjectRoot()
file: Path = root / "Data" / "DiffScreen.txt"
lines: list[str] = fileManager.LoadTxt(file)
print(lines)
