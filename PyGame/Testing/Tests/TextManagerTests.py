from Managers.TextManager import TextManager
from Screens.DiffScreen import DiffScreen
from bootstrap import build_game
from Objects.TextData import TextData


registry = build_game()

textManager = registry.get(TextManager.__name__)
#screen: str = DiffScreen.__name__
#lines: list[TextData] = textManager.InitTextData(screen)
#print(lines)

pos: tuple[int, int] = textManager.GetWhitePosition(27, 9)
print(pos)