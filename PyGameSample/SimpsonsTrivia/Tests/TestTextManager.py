from Game.Objects.TextData import TextData
from Game.Screens.DiffScreen import DiffScreen


def test_init_text_data(baseManager, textManager):
    baseManager.Initialize()
    textManager.Initialize()

    lines: list[TextData] = textManager.InitTextData(DiffScreen.__name__)

    assert lines is not None
    assert len(lines) == 12
    assert lines[4].Text == "DIFFICULTY"
