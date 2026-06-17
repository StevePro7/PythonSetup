from Game.Managers.TextManager import TextManager
from Game.Managers.BaseManager import BaseManager
from Game.Screens.DiffScreen import DiffScreen
from Engine.Bootstrap import build_game
from Game.Objects.TextData import TextData


registry = build_game()

baseManager = registry.get(BaseManager.__name__)
baseManager.Initialize()

textManager = registry.get(TextManager.__name__)
textManager.Initialize()

screen: str = DiffScreen.__name__
lines: list[TextData] = textManager.InitTextData(screen)
print(lines)

pos: tuple[int, int] = textManager.GetWhitePosition(27, 9)
print(pos)