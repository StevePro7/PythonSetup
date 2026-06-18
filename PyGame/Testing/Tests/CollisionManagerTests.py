from Game.Managers.CollisionManager import CollisionManager
from Engine.Bootstrap import build_game
from Game.Static import Enumerations as enums


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
#print(test)

#pos: tuple[int, int] = collisionManager.GetWhitePosition(27, 9)
#print(pos)

invalid: enums.OptionType = collisionManager.GetOptionType(589, 188)
assert invalid == enums.OptionType.Invalid
print(invalid)

a: enums.OptionType = collisionManager.GetOptionType(62, 195)
assert a == enums.OptionType.A
print(a)

b: enums.OptionType = collisionManager.GetOptionType(58, 275)
assert b == enums.OptionType.B
print(b)

c: enums.OptionType = collisionManager.GetOptionType(44, 342)
assert c == enums.OptionType.C
print(c)

d: enums.OptionType = collisionManager.GetOptionType(48, 437)
assert d == enums.OptionType.D
print(d)