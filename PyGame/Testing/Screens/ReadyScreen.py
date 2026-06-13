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
        self.dotsDelay: int = None
        self.diffText: str = None
        self.longText: str = None
        self.nextScreen: enumerations.ScreenType = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().Initialize()
        super().InitScreenText()

        self.dotsDelay = MyGame.Manager.ConfigManager.ConfigData.DotsDelay
        self.quizPositions = self.__getQuizPositions()


    def LoadContent(self) -> None:
        super().LoadContent()
        MyGame.Manager.SoundManager.ResumeMusic()

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
            return self.nextScreen

        super().UpdateTimer(deltaTime)
        if self.Timer > self.dotsDelay:
            self.Timer = 0
            self.dotsCount += 1
            if self.dotsCount > 3:
                self.dotsCount = 0


        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            rght: bool = MyGame.Manager.InputManager.Forward()
            if rght:
                MyGame.Manager.SoundManager.StopMusic()
                MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Ready)
                self.nextScreen = ScreenType.Play
                self.flag = True
            else:
                left: bool = MyGame.Manager.InputManager.Back()
                if left:
                    MyGame.Manager.SoundManager.StopMusic()
                    MyGame.Manager.SoundManager.PlaySound(enumerations.SoundType.Wrong)
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
        positions: list[pygame.Vector2] = []
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 7))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(2, 12))

        positions.append(MyGame.Manager.TextManager.GetTextPosition(7, 18))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(8, 18))
        positions.append(MyGame.Manager.TextManager.GetTextPosition(9, 18))
        return positions
