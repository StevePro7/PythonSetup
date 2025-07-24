import pytest
from src.app import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result["status"] == "OK"
    assert result["data"] == [42]