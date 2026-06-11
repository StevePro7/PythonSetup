import pygame
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from Objects.TextData import TextData
from enumerations import ScreenType


class ScoreScreen(BaseScreen):

    def __init__(self):
        pass
        # self.titleDelay: int = None
        # self.flash: bool = None
        # self.globalCheat: bool = None
        # self.localCheat: bool = None
        # self.cheatCount: int = None
        # self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()

        # self.textPositions: list[pygame.Vector2] = self.__getTextPositions()
        # self.whitePositions: list[pygame.Vector2] = self.__getWhitePositions()
        #
        # self.titleDelay = MyGame.Manager.ConfigManager.ConfigData.TitleDelay
        # self.flash = MyGame.Manager.ConfigManager.ConfigData.FlashTitle



    def LoadContent(self) -> None:
        super().LoadContent()
        # self.globalCheat = MyGame.Manager.ConfigManager.ConfigData.CheatMode
        # self.localCheat = self.globalCheat
        # MyGame.Manager.QuestionManager.SetCheatMode(self.localCheat)
        #
        # self.cheatCount = 0
        # self.flag = False


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateTimer(deltaTime)
        # if self.Timer > self.titleDelay:
        #     self.Timer = 0
        #     self.flag = not self.flag
        #
        # if MyGame.Manager.InputManager.Forward():
        #     MyGame.Manager.ScoreManager.Increment()

        return None


    def Draw(self) -> None:
        super().DrawScreenText()
        # MyGame.Manager.ScoreManager.DrawScore()
        #
        # # adriana - start
        # totalText = MyGame.Manager.QuestionManager.QuizLengthText2
        # solveValu = MyGame.Manager.QuestionManager.QuestionNumber
        # solveText = MyGame.Manager.BaseManager.GetNumberSP(solveValu)
        #
        # scoreValu: int = MyGame.Manager.ScoreManager.ScoreValu
        # visorValu: int = 0
        # if solveValu > 0:
        #     visorValu = int(solveValu / scoreValu * 100)
        # visorText = MyGame.Manager.BaseManager.GetNumberSP(visorValu)
        # MyGame.Manager.ScoreManager.DrawStats(totalText, solveText, visorText)
        # adriana - end


        # # Show / hide cheat mode text
        # if not self.localCheat:
        #     super().HideCheatMode()
        #
        # # Flash Press Start
        # if not self.flash or not self.flag:
        #     return
        #
        # MyGame.Manager.SpriteManager.DrawWhite(self.whitePositions[0])
        # MyGame.Manager.SpriteManager.DrawWhite(self.whitePositions[1])

    #
    # def __getTextPositions(self) -> list[pygame.Vector2]:
    #     positions: list[pygame.Vector2] = []
    #     positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 13))
    #     positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 14))
    #     return positions
    #
    #
    # def __getWhitePositions(self) -> list[pygame.Vector2]:
    #     positions: list[pygame.Vector2] = []
    #     positions.append(MyGame.Manager.TextManager.GetWhitePosition(2, 13))
    #     positions.append(MyGame.Manager.TextManager.GetWhitePosition(4, 13))
    #     return positions