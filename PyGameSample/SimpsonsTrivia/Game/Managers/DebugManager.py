from Game.MyGame import MyGame


class DebugManager:

    def SetDebugSettings(self) -> None:
        debugging: bool = MyGame.Manager.ConfigManager.ConfigData.Debugging

        difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        if difficultyType is None or debugging:
            difficultyType = MyGame.Manager.ConfigManager.ConfigData.DifficultyType
            MyGame.Manager.QuestionManager.SetDebugDifficulty(difficultyType)

        numberQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        if numberQuestion is None or debugging:
            numberQuestion = MyGame.Manager.ConfigManager.ConfigData.OptionType
            MyGame.Manager.QuestionManager.SetQuizLength(numberQuestion)
