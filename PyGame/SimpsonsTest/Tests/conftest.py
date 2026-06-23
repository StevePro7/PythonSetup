import pytest

from Engine.Bootstrap import build_game
from Game.Managers.BaseManager import BaseManager
from Game.Managers.CollisionManager import CollisionManager
from Game.Managers.ConfigManager import ConfigManager
from Game.Managers.ContentManager import ContentManager
from Game.Managers.PyGameManager import PyGameManager


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
def pyGameManager(registry):
    return registry.get(PyGameManager.__name__)