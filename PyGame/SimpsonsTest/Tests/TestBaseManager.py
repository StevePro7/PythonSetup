from pathlib import Path

from Game.Static import Constants as const
from Game.Static import Enumerations as enums


def test_get_number_zo(baseManager):
    assert baseManager.GetNumberZO(1) == "001"
    assert baseManager.GetNumberZO(12) == "012"
    assert baseManager.GetNumberZO(123) == "123"

def test_get_number_sp(baseManager):
    assert baseManager.GetNumberSP(1) == "  1"
    assert baseManager.GetNumberSP(12) == " 12"
    assert baseManager.GetNumberSP(123) == "123"

def test_get_number_custom_padding(baseManager):
    assert baseManager.GetNumber(1, " ") == "  1"
    assert baseManager.GetNumber(12, " ") == " 12"
    assert baseManager.GetNumber(123, " ") == "123"


def test_get_positions_select_count(baseManager):
    positions = baseManager.GetPositionsSelect()

    assert len(positions) == len(enums.OptionType)


def test_get_position_select(baseManager):
    pos = baseManager.GetPositionSelect(2, 3)

    expected_x = (
        const.GameOffsetX
        + 2 * const.SpriteTile
        + const.OffsetSelect
    )

    expected_y = (
        3 * const.SpriteTile
        + const.OffsetSelect
    )

    assert pos.x == expected_x
    assert pos.y == expected_y


def test_get_project_root(baseManager):
    root = baseManager.GetProjectRoot()

    assert isinstance(root, Path)
    assert (root / "pyproject.toml").exists()


def test_initialize_sets_content_root(baseManager):
    baseManager.Initialize()

    expect = baseManager.GetProjectRoot() / const.ASSETS_DIRECTORY

    assert baseManager.GetContentRoot() == expect
