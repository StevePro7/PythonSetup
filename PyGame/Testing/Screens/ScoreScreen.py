import pygame
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from enumerations import ScreenType


class ScoreScreen(BaseScreen):

    def __init__(self):
        self.totalText: str = None
        self.solveText: str = None
        self.visorText: str = None
        self.solveValu: int = None
        self.visorValu: int = None


    def Initialize(self) -> None:
        super().InitScreenText()


    def LoadContent(self) -> None:
        super().LoadContent()

        self.totalText = MyGame.Manager.QuestionManager.QuizLengthText2
        self.solveValu = MyGame.Manager.QuestionManager.QuestionNumber
        self.solveText = MyGame.Manager.BaseManager.GetNumberSP(self.solveValu)

        self.scoreValu = MyGame.Manager.ScoreManager.ScoreValu
        self.visorValu = 0
        if self.solveValu > 0:
            self.visorValu = int(self.scoreValu / self.solveValu * 100)
        self.visorText = MyGame.Manager.BaseManager.GetNumberSP(self.visorValu)


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateTimer(deltaTime)
        return None


    def Draw(self) -> None:
        #  Draw all text first.
        super().DrawScreenText()
        MyGame.Manager.QuestionManager.DrawQuizDiffText()
        MyGame.Manager.ScoreManager.DrawStats(self.totalText, self.solveText, self.visorText)

        #  Draw all images next.
        MyGame.Manager.ImageManager.DrawHeader()
        MyGame.Manager.ImageManager.DrawCurrActor()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
