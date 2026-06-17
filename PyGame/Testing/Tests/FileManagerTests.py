from Game.Managers.FileManager import FileManager
from Game.MyGame import MyGame
from Engine.Bootstrap import build_game
import Game.Static.Constants as const
from pathlib import Path


registry = build_game()

fileManager = registry.get(FileManager.__name__)
root: Path = MyGame.Manager.BaseManager.GetProjectRoot()
file: Path = root / const.ASSETS_DIRECTORY / const.DATA_DIRECTORY / const.TEXTS_DIRECTORY / "DiffScreen.txt"
lines: list[str] = fileManager.LoadTxt(file)
print(lines)
