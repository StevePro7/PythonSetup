import pygame
from pathlib import Path
from Static import Constants as const
from Static import Enumerations as enums


class BaseManager:

    def __init__(self):
        self.contentRoot: Path = None

    def Initialize(self):
        self.contentRoot: Path = self.GetProjectRoot()


    def GetContentRoot(self) -> Path:
        return self.contentRoot


    def GetNumberZO(self, number: int) -> str:
        return self.GetNumber(number, "0")

    def GetNumberSP(self, number: int) -> str:
        return self.GetNumber(number, " ")

    def GetNumber(self, number: int, paddingChar: str) -> str:
        return str(number).rjust(3, paddingChar)

    def GetPositionsSelect(self) -> list[pygame.Vector2]:
        y: int = 7
        positionsSelect: list[pygame.Vector2] = []

        for index in range(len(enums.OptionType)):
            pos: pygame.Vector2 = self.GetPositionSelect(0, y)
            positionsSelect.append(pos)
            y += 4

        return positionsSelect

    def GetPositionSelect(self, x: int, y: int) -> pygame.Vector2:
        px: int = const.GameOffsetX + x * const.SpriteTile + const.OffsetSelect
        py: int = y * const.SpriteTile + const.OffsetSelect
        return pygame.Vector2(px, py)


    def GetVolumeIconPos(self) -> pygame.Vector2:
        x: int = const.SCREEN_WIDE - const.SpriteSize - const.GameOffsetX
        y: int = -const.FONT_SIZE / 2
        return pygame.Vector2(x, y)

    def GetCheatModePos(self) -> pygame.Vector2:
        x: int = const.CheatModeOffsetX + const.GameOffsetX
        y: int = const.CheatModeOffsetY
        return pygame.Vector2(x, y)

    def GetCharacterPos(self) -> pygame.Vector2:
        x: int = const.GameOffsetX + const.FONT_SIZE * const.FONT_SIZE
        y: int = const.NUMBER_SPRITES * const.FONT_SIZE
        return pygame.Vector2(x, y)

    def GetProjectRoot(self) -> Path:
        PROJECT_TOML: str = "pyproject.toml"
        current_dir: Path = Path(__file__).parent
        project_root: Path = current_dir

        while not (project_root / PROJECT_TOML).exists() and project_root != project_root.parent:
            project_root = project_root.parent

        if not (project_root / PROJECT_TOML).exists():
            raise FileNotFoundError(f"Could not find project root with {PROJECT_TOML}")

        return project_root