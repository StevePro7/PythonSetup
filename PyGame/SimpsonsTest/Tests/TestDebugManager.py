from types import SimpleNamespace
from unittest.mock import Mock
from Game.MyGame import MyGame


def test_set_debug_settings_debug_mode_overrides(monkeypatch, debugManager):
    config_manager = SimpleNamespace(
        ConfigData=SimpleNamespace(
            Debugging=True,
            DifficultyType="Easy",
            OptionType=10,
        )
    )

    question_manager = SimpleNamespace(
        DifficultyType="Hard",
        NumberQuestion=50,
        SetDebugDifficulty=Mock(),
        SetQuizLength=Mock(),
    )

    monkeypatch.setattr(MyGame.Manager, "ConfigManager", config_manager)
    monkeypatch.setattr(MyGame.Manager, "QuestionManager", question_manager)

    debugManager.SetDebugSettings()

    question_manager.SetDebugDifficulty.assert_called_once_with("Easy")
    question_manager.SetQuizLength.assert_called_once_with(10)
