from dataclasses import dataclass
from Static.Colors import Colors

@dataclass(frozen=True)
class TextData:
    Position: pygame.Vector2
    Text: str
    Color: Colors
    #List: list[str]