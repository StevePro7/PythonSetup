from Managers.RandomManager import RandomManager
from bootstrap import build_game
from utils import get_project_root
from pathlib import Path

registry = build_game()

randomManager = registry.get(RandomManager.__name__)
#randomManager.Initialize(100)
randomManager.Initialize()
value = randomManager.Next(10)      # 0-9
value = randomManager.Next(5, 10)   # 5-9
print(value)
