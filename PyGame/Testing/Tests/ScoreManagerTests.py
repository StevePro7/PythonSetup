from Managers.ScoreManager import ScoreManager
from bootstrap import build_game
import enumerations as enums

registry = build_game()

scoreManager = registry.get(ScoreManager.__name__)

scoreManager.Initialize()
scoreManager.LoadContent()

print(scoreManager.ScoreValu)
scoreManager.Increment()
print(scoreManager.ScoreValu)