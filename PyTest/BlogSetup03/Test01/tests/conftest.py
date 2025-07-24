import pytest

@pytest.fixture
def steve_fixture():
    # setup
    yield "hello"
    # teardown


@pytest.fixture
def user_creds():
    def _user_creds(name: str, email: str):
        return {
            "name": name,
            "email": email
        }

    return _user_creds
