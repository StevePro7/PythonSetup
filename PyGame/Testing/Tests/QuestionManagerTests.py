from Managers.QuestionManager import QuestionManager
from bootstrap import build_game
from utils import get_project_root
from pathlib import Path

registry = build_game()

questionManager = registry.get(QuestionManager.__name__)