import pygame
import enumerations
from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType


class ReadyScreen(BaseScreen):

    def __init__(self):
        self.quizPositions: list[pygame.Vector2] = None
        self.difficultyType: enumerations.DifficultyType = None
        self.numberQuestion: int = None
        self.dotsCount: int = None
        self.delay: int = None
        self.delay2: int = None
        self.timer2: int = None
        self.diffText: str = None
        self.longText: str = None
        self.nextScreen: enumerations.ScreenType = None
        self.flag: bool = None

    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()

        self.quizPositions = self.__getQuizPositions()



    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()

        self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        self.numberQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        debugging: bool = MyGame.Manager.ConfigManager.ConfigData.Debugging

        if self.difficultyType is None or debugging:
            MyGame.Manager.QuestionManager.SetDifficulty(MyGame.Manager.ConfigManager.ConfigData.DifficultyType)
            self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        if self.numberQuestion is None or debugging:
            MyGame.Manager.QuestionManager.SetQuizLength(MyGame.Manager.ConfigManager.ConfigData.OptionType)
            self.numberQuestion = MyGame.Manager.ConfigManager.ConfigData.OptionType


        self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        self.numberQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        self.diffText = MyGame.Manager.QuestionManager.DifficultyText
        self.longText = MyGame.Manager.QuestionManager.QuizLengthText2

        MyGame.Manager.ScoreManager.LoadContent()
        self.dotsCount = 0
        self.timer2 = 0
        self.flag = False
        self.nextScreen = None


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateTimer(deltaTime)
        self.timer2 += deltaTime

        if self.flag:
            super().BlockOnSoundFX()
            return self.nextScreen

        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            pass

        return None


    def Draw(self) -> None:
        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()
        super().DrawScreenText()
        super().HideCheatMode()

        MyGame.Manager.TextManager.DrawTextPos(self.diffText, self.quizPositions[0])
        MyGame.Manager.TextManager.DrawTextPos(self.longText, self.quizPositions[1])

    def __getQuizPositions(self) -> list[pygame.Vector2]:
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 7))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 12))

        positions.append(MyGame.Manager.TextManager.GetTextPosition(7, 18))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(8, 18))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(9, 18))
        return positions