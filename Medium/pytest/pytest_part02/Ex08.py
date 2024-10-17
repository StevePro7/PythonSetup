import pytest


@pytest.fixture
def database_connection() -> Generator:
    conn = create_db_connection()
    yield conn
    conn.close()


def test_database_query(database_connection) -> None:
    result = database_connection.execute("SELECT * FROM users")
    assert len(result) > 0
