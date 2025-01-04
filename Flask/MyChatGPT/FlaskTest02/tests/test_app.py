import pytest
from app import app
from unittest.mock import MagicMock


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_user_service():
    return MagicMock()


def test_get_users(client, mock_user_service):
    mock_user_service.get_all_users.return_value = [{"id": 1, "name": "John", "email": "john@example.com"}]

    # Dependency Injection: Inject the mock service into the app
    app.user_service = mock_user_service

    response = client.get("/users")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "John"


def test_create_user(client, mock_user_service):
    mock_user_service.create_user.return_value = {"id": 2, "name": "Jane", "email": "jane@example.com"}

    # Inject the mock service
    app.user_service = mock_user_service

    response = client.post("/users", json={"name": "Jane", "email": "jane@example.com"})
    data = response.get_json()

    assert response.status_code == 201
    assert data["name"] == "Jane"
    assert data["email"] == "jane@example.com"
