from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Question:
    QuestionText: List[str]
    AnswerAText: List[str]
    AnswerBText: List[str]
    AnswerCText: List[str]
    AnswerDText: List[str]
    AnswerCode: int
