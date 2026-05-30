from Managers.FileManager import FileManager
from bootstrap import build_game
from utils import get_project_root
from pathlib import Path

registry = build_game()

fileManager = registry.get(FileManager.__name__)
root: Path = get_project_root()
file: Path = root / "Data" / "DiffScreen.txt"
lines: list[str] = fileManager.LoadTxt(file)
print(lines)
