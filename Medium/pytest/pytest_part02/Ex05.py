import pytest


@pytest.fixture(params=[10, 20, 30])
def data_value(request) -> int:
    return request.param


def test_data_manipulation(data_value) -> None:
    result = manipulate_data(data_value)
    assert result > data_value
