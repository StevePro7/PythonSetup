import pytest
import sys


@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature() -> None:
    # This test will be skipped
    pass


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python 3.7+")
def test_new_feature() -> None:
    # This test will only run on Python 3.7 and above
    pass


@pytest.mark.xfail(reason="Known bug")
def test_failing_feature() -> None:
    assert 1 == 2  # This failure won't cause the test run to fail