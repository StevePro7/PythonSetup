import http

from fastapi.testclient import TestClient

client = TestClient(app)

def test_endpoint_returns_correct_data() -> None:
    response = client.get("/endpoint")
    assert http.HTTPStatus.OK == response.status_code
    assert response.json() = {"ley": "value"}