from Managers.CollisionManager import CollisionManager
from bootstrap import build_game

registry = build_game()

collisionManager = registry.get(CollisionManager.__name__)
#screen: str = DiffScreen.__name__
#lines: list[TextData] = textManager.InitTextData(screen)
#print(lines)
collisionManager.LoadContent()

#test: bool = collisionManager.FullScreen(20, 20)
#test: bool = collisionManager.VolumeIcon(560, 20)
test: bool = collisionManager.CheatMode(430, 260)
test: bool = collisionManager.Character(400, 160)

# test: enums.OptionType = collisionManager.GetOptionType(20, 400)
print(test)

#pos: tuple[int, int] = collisionManager.GetWhitePosition(27, 9)
#print(pos)