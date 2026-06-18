from Game.MyGame import MyGame


class DebugManager:

    def SetDebugSettings(self) -> None:
        if MyGame.Manager.QuestionManager.DifficultyType is None:
            MyGame.Manager.QuestionManager.SetDifficulty(MyGame.Manager.ConfigManager.ConfigData.DifficultyType)

        if MyGame.Manager.QuestionManager.NumberQuestion is None:
            MyGame.Manager.QuestionManager.SetQuizLength(MyGame.Manager.ConfigManager.ConfigData.OptionType)
