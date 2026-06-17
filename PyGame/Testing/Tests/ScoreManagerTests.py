from Game.Managers.ScoreManager import ScoreManager
from Engine.Bootstrap import build_game


registry = build_game()

scoreManager = registry.get(ScoreManager.__name__)

scoreManager.Initialize()
scoreManager.LoadContent()

print(scoreManager.ScoreValu)
scoreManager.Increment()
print(scoreManager.ScoreValu)