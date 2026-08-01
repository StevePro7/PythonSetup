import pygame
from Game.MyGame import MyGame


class ScoreManager:

    def __init__(self):
        self.ScoreValu: int = None
        self.scoreText: str = None
        self.valueText: str = None
        self.scorePosn: pygame.Vector2 = None

        self.totalPosn: pygame.Vector2 = None
        self.solvePosn: pygame.Vector2 = None
        self.rightPosn: pygame.Vector2 = None
        self.visorPosn: pygame.Vector2 = None


    def Initialize(self):
        self.scorePosn = self.__getScorePosn()
        self.__calculatePositions()


    def LoadContent(self):
        self.Reset()


    def Increment(self) -> None:
        self.ScoreValu += 1
        self.__setText()


    def DrawScore(self) -> None:
        MyGame.Manager.TextManager.DrawTextPos(self.scoreText, self.scorePosn)

    def DrawStats(self, totalText: str, solveText: str, visorText: str) -> None:
        MyGame.Manager.TextManager.DrawTextPos(totalText, self.totalPosn)
        MyGame.Manager.TextManager.DrawTextPos(solveText, self.solvePosn)
        MyGame.Manager.TextManager.DrawTextPos(self.valueText, self.rightPosn)
        MyGame.Manager.TextManager.DrawTextPos(visorText, self.visorPosn)


    def Reset(self) -> None:
        self.ScoreValu = 0
        self.__setText()


    def __setText(self) -> None:
        self.scoreText = MyGame.Manager.BaseManager.GetNumberZO(self.ScoreValu)
        self.valueText = MyGame.Manager.BaseManager.GetNumberSP(self.ScoreValu)

    def __getScorePosn(self) -> pygame.Vector2:
        return MyGame.Manager.TextManager.GetTextPosition(29, 3)

    def __calculatePositions(self) -> None:
        self.totalPosn = MyGame.Manager.TextManager.GetTextPosition(17, 6)
        self.solvePosn = MyGame.Manager.TextManager.GetTextPosition(17, 10)
        self.rightPosn = MyGame.Manager.TextManager.GetTextPosition(17, 14)
        self.visorPosn = MyGame.Manager.TextManager.GetTextPosition(17, 18)
