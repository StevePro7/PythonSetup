import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.controllers.user_service')
def test_get_users(mock_user_service, client):
    mock_user_service.get_all_users.return_value = []
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == []
