import pytest

from Engine.Bootstrap import build_game
from Game.Managers.BaseManager import BaseManager
from Game.Managers.CollisionManager import CollisionManager
from Game.Managers.ConfigManager import ConfigManager
from Game.Managers.FileManager import FileManager
from Game.Managers.ImageManager import ImageManager
from Game.Managers.PyGameManager import PyGameManager
from Game.Managers.QuestionManager import QuestionManager
from Game.Managers.RandomManager import RandomManager
from Game.Managers.ScoreManager import ScoreManager
from Game.Managers.SoundManager import SoundManager
from Game.Managers.TextManager import TextManager
from Game.Managers.ContentManager import ContentManager


@pytest.fixture
def baseManager(registry):
    return registry.get(BaseManager.__name__)

@pytest.fixture
def baseManager(registry):
    return registry.get(BaseManager.__name__)


@pytest.fixture(scope="session")
def registry():
    return build_game()


@pytest.fixture
def baseManager(registry):
    return registry.get(BaseManager.__name__)


@pytest.fixture
def collisionManager(registry):
    return registry.get(CollisionManager.__name__)


@pytest.fixture
def configManager(registry):
    return registry.get(ConfigManager.__name__)


@pytest.fixture
def contentManager(registry):
    return registry.get(ContentManager.__name__)


@pytest.fixture
def fileManager(registry):
    return registry.get(FileManager.__name__)

@pytest.fixture
def imageManager(registry):
    return registry.get(ImageManager.__name__)


@pytest.fixture
def pyGameManager(registry):
    return registry.get(PyGameManager.__name__)


@pytest.fixture
def questionManager(registry):
    return registry.get(QuestionManager.__name__)


@pytest.fixture
def randomManager(registry):
    return registry.get(RandomManager.__name__)


@pytest.fixture
def scoreManager(registry):
    return registry.get(ScoreManager.__name__)


@pytest.fixture
def soundManager(registry):
    return registry.get(SoundManager.__name__)


@pytest.fixture
def textManager(registry):
    return registry.get(TextManager.__name__)
