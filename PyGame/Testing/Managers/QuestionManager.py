import pygame
from MyGame import MyGame
from Objects.Question import Question

class QuestionManager:

    def __init__(self):
        self.questionRoot: str = None
        self.questionPosn: list[pygame.Vector2] = None
        self.answerAPosn: list[pygame.Vector2] = None; self.answerBPosn: list[pygame.Vector2] = None; self.answerCPosn: list[pygame.Vector2] = None; self.answerDPosn: list[pygame.Vector2] = None
        self.originAPosn: list[pygame.Vector2] = None; self.originBPosn: list[pygame.Vector2] = None; self.originCPosn: list[pygame.Vector2] = None; self.originDPosn: list[pygame.Vector2] = None
        self.numberPos: pygame.Vector2 = None; totalPos: pygame.Vector2 = None; diffPos: pygame.Vector2 = None
        self.numberTxt: str = None
        self.answerList: list[int] = None
        self.cheatMode: bool = False


    def Initialize(self):
        self.semicolon = ";"
        self.pipe = "|"


    def LoadQuestion(self, line: str):
        texts: list[str] = line.split(self.semicolon)

        questionText: list[str] = texts[1].split(self.pipe)
        answerAText: list[str] = texts[2].split(self.pipe)
        answerBText: list[str] = texts[3].split(self.pipe)
        answerCText: list[str] = texts[4].split(self.pipe)
        answerDText: list[str] = texts[5].split(self.pipe)
        answerCode: int = int(texts[0])

        return Question(questionText, answerAText, answerBText, answerCText, answerDText, answerCode)




    def LoadContent(self):
        pass

    def Update(self, deltaTime: int):
        pass

    def Draw(self):
        pass
