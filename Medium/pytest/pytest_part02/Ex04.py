import pytest


@pytest.fixture(autouse=True)
def setup_database() -> Generator:
    # Set up database
    yield
    # Tear down database


def test_database_query() -> None:
    # This test will automatically use the setup_database fixture
    assert query_database() == expected_result