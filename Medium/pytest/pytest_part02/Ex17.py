import pytest
import asyncio


@pytest.mark.asyncio
async def test_async_function() -> None:
    result = await async_function()
    assert result == "expected result"



@pytest.mark.order(2)
def test_second() -> None:
    pass


@pytest.mark.order(1)
def test_first() -> None:
    pass