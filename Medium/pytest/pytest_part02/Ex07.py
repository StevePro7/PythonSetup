import pytest


@pytest.fixture
def user() -> dict:
    return {"id": 1, "name": "John Doe"}


@pytest.fixture
def user_with_posts(user) -> dict:
    user["posts"] = ["Post 1", "Post 2"]
    return user


def test_user_posts(user_with_posts) -> None:
    assert len(user_with_posts["posts"]) == 2