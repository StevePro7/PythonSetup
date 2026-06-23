from pathlib import Path

from Game.Static import Constants as const


def test_get_number_zo(baseManager):
    assert baseManager.GetNumberZO(1) == "001"
    assert baseManager.GetNumberZO(12) == "012"
    assert baseManager.GetNumberZO(123) == "123"


def test_get_project_root(baseManager):
    root = baseManager.GetProjectRoot()

    assert isinstance(root, Path)
    assert (root / "pyproject.toml").exists()


def test_initialize_sets_content_root(baseManager):
    baseManager.Initialize()

    expect = baseManager.GetProjectRoot() / const.ASSETS_DIRECTORY

    assert baseManager.GetContentRoot() == expect