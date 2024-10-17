import http

from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_user() -> None:
    response = client.post(
        "/users", json={"name": "John Doe", "email": "john@example.com"}
    )
    assert http.HTTPStatus.CREATED == response.status_code
    assert response.json()["name"] = "John Doe"