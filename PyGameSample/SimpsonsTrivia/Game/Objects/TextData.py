from dataclasses import dataclass
from Game.Static.Colors import Colors


@dataclass(frozen=True)
class TextData:
    Position: tuple[int, int]
    Text: str
    Color: Colors
