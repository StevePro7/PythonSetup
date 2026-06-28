from Game.Static import Enumerations as enums


def test_load_question_list(baseManager, configManager, randomManager, questionManager):
    baseManager.Initialize()

    configManager.Initialize()
    configManager.LoadContent()

    randomManager.Initialize()

    questionManager.Initialize()

    questionManager.LoadQuestionList(enums.DifficultyType.Norm)

    assert questionManager.QuestionList is not None
    assert questionManager.QuestionList[0].AnswerCode == 1