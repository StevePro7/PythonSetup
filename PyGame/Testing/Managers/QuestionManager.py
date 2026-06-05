import pygame
from pathlib import Path
from MyGame import MyGame
from Objects.Question import Question
import constants as const
import enumerations as enums
import utils


class QuestionManager:

    def __init__(self):
        # Private members.
        self.questionPosn: list[pygame.Vector2] = None
        self.answerAPosn: list[pygame.Vector2] = None; self.answerBPosn: list[pygame.Vector2] = None; self.answerCPosn: list[pygame.Vector2] = None; self.answerDPosn: list[pygame.Vector2] = None
        self.originAPosn: list[pygame.Vector2] = None; self.originBPosn: list[pygame.Vector2] = None; self.originCPosn: list[pygame.Vector2] = None; self.originDPosn: list[pygame.Vector2] = None
        self.numberPos: pygame.Vector2 = None; self.totalPos: pygame.Vector2 = None; self.diffPos: pygame.Vector2 = None
        self.numberTxt: str = None
        self.answerList: list[int] = None
        self.cheatMode: bool = None

        # Properties
        self.QuestionList: list[Question] = None
        self.QuestionNumber: int = None
        self.NumberQuestion: int = None
        self.DifficultyType: enums.DifficultyType = None
        self.CorrectOptionType: enums.OptionType = None
        self.DifficultyText: str = None
        self.QuizLengthText: str = None
        self.QuizLengthText2: str = None


    def Initialize(self):
        self.semicolon = ";"
        self.pipe = "|"

        self.answerList: list[int] = []
        self.QuestionList: list[Question] = []
        self.cheatMode: bool = False


    def LoadContent(self):
        self.questionPosn = self.GetQuestionPosn()
        self.answerAPosn = self.GetAnswerAPosn()
        self.answerBPosn = self.GetAnswerBPosn()
        self.answerCPosn = self.GetAnswerCPosn()
        self.answerDPosn = self.GetAnswerDPosn()

        self.originAPosn = self.answerAPosn
        self.originBPosn = self.answerBPosn
        self.originCPosn = self.answerCPosn
        self.originDPosn = self.answerDPosn

        self.numberPos = MyGame.Manager.TextManager.GetTextPosition(12, 3)
        self.totalPos = MyGame.Manager.TextManager.GetTextPosition(16, 3);
        self.diffPos = MyGame.Manager.TextManager.GetTextPosition(2, 1);

        self.Reset()


    def LoadQuestionList(self, type: enums.DifficultyType) -> None:
        self.QuestionList.clear()

        file: str = self.__getTextFile(type)
        lines: list[str] = MyGame.Manager.FileManager.LoadTxt(file)
        for line in lines:
            question: Question = self.LoadQuestion(line)
            self.QuestionList.append(question)


    def PlayQuestion(self, index: int) -> Question:
        q: Question = self.QuestionList[index]
        answerCode: int = q.AnswerCode
        answerCode -= 1

        # Set correct option for this question.
        self.CorrectOptionType: enums.OptionType = enums.OptionType(answerCode)
        return q


    def LoadQuestion(self, line: str):
        texts: list[str] = line.split(self.semicolon)

        questionText: list[str] = texts[1].split(self.pipe)
        answerAText: list[str] = texts[2].split(self.pipe)
        answerBText: list[str] = texts[3].split(self.pipe)
        answerCText: list[str] = texts[4].split(self.pipe)
        answerDText: list[str] = texts[5].split(self.pipe)
        answerCode: int = int(texts[0])

        return Question(questionText, answerAText, answerBText, answerCText, answerDText, answerCode)





    def GetQuestionPosn(self) -> list[pygame.Vector2]:
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 5))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 6))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 7))
        return positions

    def GetAnswerAPosn(self) -> list[pygame.Vector2]:
        answerPosn: list[pygame.Vector2] = []
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 9))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 10))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 11))
        return answerPosn

    def GetAnswerBPosn(self) -> list[pygame.Vector2]:
        answerPosn: list[pygame.Vector2] = []
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 13))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 14))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 15))
        return answerPosn

    def GetAnswerCPosn(self) -> list[pygame.Vector2]:
        answerPosn: list[pygame.Vector2] = []
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 17))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 18))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 19))
        return answerPosn

    def GetAnswerDPosn(self) -> list[pygame.Vector2]:
        answerPosn: list[pygame.Vector2] = []
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 21))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 22))
        answerPosn.append(MyGame.Manager.TextManager.GetTextPosition(4, 23))
        return answerPosn

    def Reset(self):
        self.QuestionNumber = 0
        self.numberTxt = MyGame.Manager.BaseManager.GetNumberZO(self.QuestionNumber + 1)


    def __getTextFile(self, type: enums.DifficultyType) -> str:
        name: str = f"{type.name}.txt"
        root: Path = utils.get_project_root()
        file: Path = root / "Levels" / name
        return file