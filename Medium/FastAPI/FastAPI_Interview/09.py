# 9. Testing with FastAPI
from fastapi.testclient import TestClient
from fastapi import FastAPI
from http import HTTPStatus
"""from main import app"""

app = FastAPI()


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Welcome to FastAPI!"}
