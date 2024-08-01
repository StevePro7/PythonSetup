import pytest

# IMPORTANT
# input_value is now in the global conftest.py file

def test_divisible_by_13(input_value: int):
    assert input_value % 13 == 0
