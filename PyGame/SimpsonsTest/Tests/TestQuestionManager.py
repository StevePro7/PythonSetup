import pytest
from Game.Objects.Question import Question
from Game.Static import Enumerations as enums


@pytest.fixture
def setup_tests(baseManager, configManager, randomManager, questionManager):
    baseManager.Initialize()

    configManager.Initialize()
    configManager.LoadContent()

    randomManager.Initialize()
    questionManager.Initialize()


def test_load_question_list(setup_tests, questionManager):
    questionManager.LoadQuestionList(enums.DifficultyType.Norm)

    assert questionManager.QuestionList is not None
    assert questionManager.QuestionList[0].AnswerCode == 1


def test_play_question(setup_tests, questionManager):
    questionManager.LoadQuestionList(enums.DifficultyType.Norm)
    q: Question = questionManager.PlayQuestion(0)

    assert q is not None
    assert q.QuestionText[1] == "SPRINGFIELD?"
    assert q.AnswerCode == 1


def test_load_question(setup_tests, questionManager):
    q: Question = questionManager.LoadQuestion("1;NAME THE CINEMA IN|SPRINGFIELD?;GOOGOLPLEX;MONTIES MOVIES;MEGA MOVIES;SPRINGFIELD|SCREEN;page01;02-GeneralSimpsonsTrivia.csv")

    assert q is not None
    assert q.QuestionText[1] == "SPRINGFIELD?"
    assert q.AnswerCode == 1


def test_set_difficulty(setup_tests, questionManager):
    questionManager.SetDifficulty(enums.OptionType.B)

    assert questionManager.DifficultyType == enums.DifficultyType.Norm
    assert questionManager.DifficultyText == "NORM"


def test_set_quiz_length(setup_tests, questionManager):
    questionManager.SetQuizLength(enums.OptionType.B)

    assert questionManager.NumberQuestion == 10
    assert questionManager.QuizLengthText == "010"
    assert questionManager.QuizLengthText2 == " 10"


def test_increment(setup_tests, questionManager):
    questionManager.SetQuizLength(enums.OptionType.B)
    questionManager.Reset()
    assert questionManager.QuestionNumber == 0

    questionManager.Increment()
    assert questionManager.QuestionNumber == 1
