# test_snowflake_db.py
import pytest
from unittest.mock import patch, MagicMock
from snowflake_db import SnowflakeDB


@patch("snowflake_db.snowflake.connector.connect")
def test_snowflake_db_workflow(mock_connect):
    # Arrange: Create fake connection and cursor
    fake_conn = MagicMock()
    fake_cursor = MagicMock()
    fake_cursor.fetchall.return_value = [("row1",), ("row2",)]

    fake_conn.cursor.return_value = fake_cursor
    mock_connect.return_value = fake_conn

    # Act
    db = SnowflakeDB(
        user="test_user",
        password="test_pass",
        account="test_account",
        warehouse="test_warehouse",
        database="test_db",
        schema="test_schema"
    )

    db.open_connection()
    result = db.execute_query("SELECT * FROM users")
    db.close_connection()

    # Assert
    mock_connect.assert_called_once_with(
        user="test_user",
        password="test_pass",
        account="test_account",
        warehouse="test_warehouse",
        database="test_db",
        schema="test_schema"
    )
    fake_cursor.execute.assert_called_once_with("SELECT * FROM users")
    fake_cursor.fetchall.assert_called_once()
    fake_cursor.close.assert_called_once()
    fake_conn.close.assert_called_once()

    assert result == [("row1",), ("row2",)]
