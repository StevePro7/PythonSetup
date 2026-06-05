from Managers.CollisionManager import CollisionManager
from bootstrap import build_game

registry = build_game()

collisionManager = registry.get(CollisionManager.__name__)
#screen: str = DiffScreen.__name__
#lines: list[TextData] = textManager.InitTextData(screen)
#print(lines)
collisionManager.LoadContent()
#pos: tuple[int, int] = collisionManager.GetWhitePosition(27, 9)
#print(pos)