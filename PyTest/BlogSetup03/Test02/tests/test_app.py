import pytest
from src.app import get_app_mode

def test_get_app_mode(monkeypatch):
    monkeypatch.setenv("APP_MODE", "Testing")
    assert get_app_mode() == "testing"
