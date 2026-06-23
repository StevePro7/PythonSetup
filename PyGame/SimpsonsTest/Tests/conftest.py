import pytest

from Engine.Bootstrap import build_game
from Game.Managers.BaseManager import BaseManager
from Game.Managers.CollisionManager import CollisionManager


@pytest.fixture(scope="session")
def registry():
    return build_game()


@pytest.fixture
def baseManager(registry):
    return registry.get(BaseManager.__name__)


@pytest.fixture
def collisionManager(registry):
    return registry.get(CollisionManager.__name__)