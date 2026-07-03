from pathlib import Path
from Game.Static import Constants as const


def test_file_manager_load_txt(baseManager, fileManager):
    path: Path = baseManager.GetProjectRoot() / const.ASSETS_DIRECTORY / const.DATA_DIRECTORY / const.LEVELS_DIRECTORY
    file: str = path / "Argh.txt"
    lines: list[str] = fileManager.LoadTxt(file)
    assert 50 == len(lines)