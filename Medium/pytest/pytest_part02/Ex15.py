import pytest
import json


# Indirect Parametrization
@pytest.fixture
def data(request) -> int:
    return request.param * 2


@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_indirect(data) -> None:
    assert data % 2 == 0



# Parametrizing Fixtures
@pytest.fixture(params=[1, 2, 3])
def data(request) -> int:
    return request.param


def test_fixture_param(data) -> None:
    assert data < 4


# Parametrization with External Data
def load_test_data(file_path) -> dict:
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.mark.parametrize("input,expected", load_test_data('test_data.json'))
def test_function(input, expected) -> None:
    assert function_under_test(input) == expected