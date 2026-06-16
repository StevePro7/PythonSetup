from Managers.QuestionManager import QuestionManager
from Managers.ConfigManager import ConfigManager
from Managers.RandomManager import RandomManager
from bootstrap import build_game
from Static import Enumerations as enums

registry = build_game()

configManager = registry.get(ConfigManager.__name__)
configManager.Initialize()
configManager.LoadContent()

randomManager = registry.get(RandomManager.__name__)
randomManager.Initialize()

questionManager = registry.get(QuestionManager.__name__)
questionManager.Initialize()
questionManager.LoadContent()


#q: Question = questionManager.PlayQuestion(0)
#print(q)
# TEST
# line: str = "3;WHO SHOT MR. BURNS?;BART;HOMER;MAGGIE;LISA;page01;02-GeneralSimpsonsTrivia.csv"
# question: Question = questionManager.LoadQuestion(line)
# assert question is not None

#questionManager.SetDifficulty(enums.OptionType.D)
#print(questionManager.QuestionList)
#print(questionManager.QuestionNumber)
#print(questionManager.NumberQuestion)
#print(questionManager.DifficultyType)
#print(questionManager.DifficultyText)

questionManager.SetQuizLength(enums.OptionType.D)
# print(questionManager.NumberQuestion)
# print(questionManager.QuizLengthText)
# print(questionManager.QuizLengthText2)

#questionManager.Increment()

# test: bool = questionManager.GetCheatMode()
# print(test)
# questionManager.SetCheatMode(True)
# test2: bool = questionManager.GetCheatMode()
# print(test2)

questionManager.Reset()
questionManager.LoadQuestionList(enums.DifficultyType.Easy)
#questionManager.RandomizeQuestionList()
#questionManager.PrintQuestionList()

index: int = 0
#questionManager.PrintAnswerList(index)
print("")

questionManager.RandomizeAnswerList(index)
#questionManager.PrintAnswerList(index)
