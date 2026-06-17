import pygame
from Game.MyGame import MyGame
from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Enumerations import ScreenType
from Game.Static import Enumerations as enums, Constants as const


class ReadyScreen(BaseScreen):

    def __init__(self):
        self.quizPositions: list[pygame.Vector2] = None
        self.difficultyType: enums.DifficultyType = None
        self.numberQuestion: int = None
        self.dotsCount: int = None
        self.dotsDelay: int = None
        self.diffText: str = None
        self.longText: str = None
        self.nextScreen: enums.ScreenType = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()

        self.dotsDelay = MyGame.Manager.ConfigManager.ConfigData.DotsDelay
        self.quizPositions = self.__getQuizPositions()


    def LoadContent(self) -> None:
        super().LoadContent()

        # adriana move this code to DebugManager begin
        self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        self.numberQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        debugging: bool = MyGame.Manager.ConfigManager.ConfigData.Debugging

        if self.difficultyType is None or debugging:
            MyGame.Manager.QuestionManager.SetDifficulty(MyGame.Manager.ConfigManager.ConfigData.DifficultyType)
            self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        if self.numberQuestion is None or debugging:
            MyGame.Manager.QuestionManager.SetQuizLength(MyGame.Manager.ConfigManager.ConfigData.OptionType)
            self.numberQuestion = MyGame.Manager.ConfigManager.ConfigData.OptionType
        # adriana move this code to DebugManager -end-

        self.difficultyType = MyGame.Manager.QuestionManager.DifficultyType
        self.numberQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        self.diffText = MyGame.Manager.QuestionManager.DifficultyText
        self.longText = MyGame.Manager.QuestionManager.QuizLengthText2

        MyGame.Manager.ScoreManager.LoadContent()
        self.dotsCount = 0
        self.flag = False
        self.nextScreen = None


    def Update(self, deltaTime: int) -> ScreenType | None:
        if self.flag:
            super().BlockOnSoundFX()
            if self.nextScreen != ScreenType.Long:
                MyGame.Manager.SoundManager.StopMusic()
            return self.nextScreen

        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            super().UpdateTimer(deltaTime)
            if self.Timer > self.dotsDelay:
                self.Timer = 0
                self.dotsCount += 1
                if self.dotsCount > const.MAX_DOTS:
                    self.dotsCount = const.MAX_DOTS
                    MyGame.Manager.SoundManager.PlaySound(enums.SoundType.Ready)
                    self.nextScreen = ScreenType.Play
                    self.flag = True

            if not self.flag:
                rght: bool = MyGame.Manager.InputManager.Forward()
                if rght:
                    MyGame.Manager.SoundManager.PlaySound(enums.SoundType.Ready)
                    self.nextScreen = ScreenType.Play
                    self.flag = True
                else:
                    left: bool = MyGame.Manager.InputManager.Back()
                    if left:
                        MyGame.Manager.SoundManager.PlaySound(enums.SoundType.Wrong)
                        self.nextScreen = ScreenType.Long
                        self.flag = True

            if self.flag:
                MyGame.Manager.QuestionManager.Reset()
                MyGame.Manager.QuestionManager.LoadQuestionList(self.difficultyType)

                if MyGame.Manager.ConfigManager.ConfigData.RandomQuestions:
                    MyGame.Manager.QuestionManager.RandomizeQuestionList()

        return None


    def Draw(self) -> None:
        super().DrawScreenText()
        super().HideCheatMode()

        MyGame.Manager.TextManager.DrawTextPos(self.diffText, self.quizPositions[0])
        MyGame.Manager.TextManager.DrawTextPos(self.longText, self.quizPositions[1])
        MyGame.Manager.TextManager.DrawTextPos(" ", self.quizPositions[1])
        self.DrawDots()

        MyGame.Manager.ImageManager.DrawTitle()
        MyGame.Manager.SoundManager.DrawVolumeIcon()


    def DrawDots(self):
        posn: int = 2
        MyGame.Manager.TextManager.DrawTextPos("   ", self.quizPositions[posn])
        for loop in range(self.dotsCount):
            MyGame.Manager.TextManager.DrawTextPos(".", self.quizPositions[posn + loop])


    def __getQuizPositions(self) -> list[pygame.Vector2]:
        coordinates: list[tuple] = [
            (2, 7),
            (2, 12),
            (7, 18),
            (8, 18),
            (9, 18),
        ]
        positions: list[pygame.Vector2] = super().GetTextPositions(coordinates)
        return positions
