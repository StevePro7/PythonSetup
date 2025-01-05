import pytest
from unittest.mock import Mock
from app.services import UserService
from app.models import User

@pytest.fixture
def mock_repository():
    return Mock()

@pytest.fixture
def user_service(mock_repository):
    return UserService(mock_repository)

def test_get_all_users(user_service, mock_repository):
    mock_repository.get_all.return_value = [User(id=1, name="John Doe", email="john@example.com")]
    users = user_service.get_all_users()
    assert len(users) == 1
    assert users[0].name == "John Doe"

def test_create_user(user_service, mock_repository):
    mock_repository.create.return_value = User(id=1, name="Jane Doe", email="jane@example.com")
    user = user_service.create_user("Jane Doe", "jane@example.com")
    assert user.name == "Jane Doe"
