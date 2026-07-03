import pygame
from pathlib import Path
from Game.MyGame import MyGame
from Game.Objects.Question import Question
from Game.Static.Globalize import Globalize
from Game.Static import Enumerations as enums, Constants as const


class QuestionManager:

    def __init__(self):
        self.contentRoot: Path = None
        self.levelsRoot: Path = None

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
        self.contentRoot = MyGame.Manager.BaseManager.GetContentRoot()
        self.levelsRoot = self.contentRoot / const.DATA_DIRECTORY / const.LEVELS_DIRECTORY

        self.semicolon = ";"
        self.pipe = "|"

        self.answerList: list[int] = []
        self.QuestionList: list[Question] = []
        self.cheatMode: bool = MyGame.Manager.ConfigManager.ConfigData.CheatMode


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


    def LoadQuestion(self, line: str) -> Question:
        texts: list[str] = line.split(self.semicolon)

        questionText: list[str] = texts[1].split(self.pipe)
        answerAText: list[str] = texts[2].split(self.pipe)
        answerBText: list[str] = texts[3].split(self.pipe)
        answerCText: list[str] = texts[4].split(self.pipe)
        answerDText: list[str] = texts[5].split(self.pipe)
        answerCode: int = int(texts[0])

        return Question(questionText, answerAText, answerBText, answerCText, answerDText, answerCode)


    def RandomizeQuestionList(self):
        list: list[Question] = self.QuestionList

        # https://stackoverflow.com/questions/273313/randomize-a-listt
        n: int = len(self.QuestionList)
        while n > 1:
            n -= 1
            k: int = MyGame.Manager.RandomManager.Next(n + 1)
            value: Question = list[k]
            list[k] = list[n]
            list[n] = value

        self.QuestionList = list


    def RandomizeAnswerList(self, index: int) -> None:
        # Get answer code first
        #  Stored as 1-4 for A-D
        q: Question = self.QuestionList[index]
        self.answerCode: int = q.AnswerCode
        self.answerCode -= 1

        self.answerList = []
        selects: int = const.NUMBER_SELECTS
        for idx in range(selects):
            self.answerList.append(0)

        # Randomize answers for question.
        # + record correct random option.
        self.CorrectOptionType = enums.OptionType.Invalid
        for idx in range(selects):
            while True:
                rnd: int = MyGame.Manager.RandomManager.Next(selects)
                if 0 == self.answerList[rnd]:
                    self.answerList[rnd] = idx
                    break

        # Set the correct option at end of loop.
        for idx in range(selects):
            val: int = self.answerList[idx]
            if self.answerCode == val:
                self.CorrectOptionType = enums.OptionType(idx)
                break

        self.RandomizeAnswerPosn()


    def DrawQuestion(self, index: int) -> None:
        if index >= self.NumberQuestion:
            return

        question: Question = self.QuestionList[index]
        for line in range(const.NUMBER_LINES):
            if line < len(question.QuestionText):
                self.DrawLine(question.QuestionText[line], self.questionPosn[line])

            if line < len(question.AnswerAText):
                self.DrawLine(question.AnswerAText[line], self.answerAPosn[line])
            if line < len(question.AnswerBText):
                self.DrawLine(question.AnswerBText[line], self.answerBPosn[line])
            if line < len(question.AnswerCText):
                self.DrawLine(question.AnswerCText[line], self.answerCPosn[line])
            if line < len(question.AnswerDText):
                self.DrawLine(question.AnswerDText[line], self.answerDPosn[line])


    def DrawQuestionNumber(self):
        MyGame.Manager.TextManager.DrawTextPos(self.numberTxt, self.numberPos)

    def DrawQuestionTotal(self):
        MyGame.Manager.TextManager.DrawTextPos(self.QuizLengthText, self.totalPos)

    def DrawQuizDiffText(self) -> None:
        MyGame.Manager.TextManager.DrawTextPos(self.DifficultyText, self.diffPos)


    def SetDebugDifficulty(self, difficultyType: enums.DifficultyType) -> None:
        self.DifficultyType = difficultyType
        index: int = difficultyType.value
        self.DifficultyText = Globalize.DIFF_TEXT[index]


    def SetDifficulty(self, optionType: enums.OptionType) -> None:
        if optionType == enums.OptionType.B:
            self.DifficultyType = enums.DifficultyType.Norm
        elif optionType == enums.OptionType.C:
            self.DifficultyType = enums.DifficultyType.Hard
        elif optionType == enums.OptionType.D:
            self.DifficultyType = enums.DifficultyType.Argh
        else:
            self.DifficultyType = enums.DifficultyType.Easy

        index: int = optionType.value
        self.DifficultyText = Globalize.DIFF_TEXT[index]


    def SetQuizLength(self, optionType: enums.OptionType) -> None:
        index = optionType.value
        self.NumberQuestion = const.QUIZ_LONG[index]
        self.QuizLengthText = MyGame.Manager.BaseManager.GetNumberZO(self.NumberQuestion)
        self.QuizLengthText2 = MyGame.Manager.BaseManager.GetNumberSP(self.NumberQuestion)


    def Increment(self):
        qNo: int = self.QuestionNumber + 1
        if qNo > self.NumberQuestion:
            return

        self.QuestionNumber += 1
        self.numberTxt = MyGame.Manager.BaseManager.GetNumberZO(self.QuestionNumber + 1)


    def Reset(self):
        self.QuestionNumber = 0
        self.numberTxt = MyGame.Manager.BaseManager.GetNumberZO(self.QuestionNumber + 1)


    def GetCheatMode(self) -> bool:
        return self.cheatMode

    def SetCheatMode(self, theCheatMode: bool) -> None:
        self.cheatMode = theCheatMode

    def DrawLine(self, line: str, posn: pygame.Vector2) -> None:
        if not line or len(line) == 0:
            return

        MyGame.Manager.TextManager.DrawTextPos(line, posn)


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


    def RandomizeAnswerPosn(self) -> None:
        origin: pygame.Vector2 = []
        for index in range(const.NUMBER_SELECTS):
            match index:
                case 0:
                    origin = self.originAPosn
                case 1:
                    origin = self.originBPosn
                case 2:
                    origin = self.originCPosn
                case 3:
                    origin = self.originDPosn

            value: int = self.answerList[index]
            match value:
                case 0:
                    self.answerAPosn = origin
                case 1:
                    self.answerBPosn = origin
                case 2:
                    self.answerCPosn = origin
                case 3:
                    self.answerDPosn = origin


    def PrintQuestionList(self) -> None:
        for question in self.QuestionList:
            print(question.QuestionText)

    def PrintAnswerList(self, index: int) -> None:
        question: Question = self.QuestionList[index]
        print(question.AnswerAText)
        print(question.AnswerBText)
        print(question.AnswerCText)
        print(question.AnswerDText)


    def __getTextFile(self, type: enums.DifficultyType) -> str:
        name: str = f"{type.name}.txt"
        file: Path = self.levelsRoot / name
        return file