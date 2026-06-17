from Managers.RandomManager import RandomManager
from Engine.Bootstrap import build_game


registry = build_game()

randomManager = registry.get(RandomManager.__name__)
#randomManager.Initialize(100)
randomManager.Initialize()
value = randomManager.Next(10)      # 0-9
value = randomManager.Next(5, 10)   # 5-9
print(value)
