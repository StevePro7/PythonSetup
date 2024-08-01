import pytest

# IMPORTANT
# input_value is now in the global conftest.py file

def test_divisible_by_3(input_value: int):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value: int):
    assert input_value % 6 == 3
