import pytest
from typing import Generator

@pytest.fixture
def temp_file(tmp_path) -> Generator:
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write("Test content")
    yield file_path
    os.remove(file_path)


def test_file_content(temp_file) -> None:
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "Test content"