from Managers.QuestionManager import QuestionManager
from bootstrap import build_game
from Objects.Question import Question

registry = build_game()

questionManager = registry.get(QuestionManager.__name__)
questionManager.Initialize()
questionManager.LoadContent()

# line: str = "3;WHO SHOT MR. BURNS?;BART;HOMER;MAGGIE;LISA;page01;02-GeneralSimpsonsTrivia.csv"
# question: Question = questionManager.LoadQuestion(line)
# assert question is not None

print("fin!!")