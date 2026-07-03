import time
from Game.MyGame import MyGame
from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Enumerations import ScreenType
from Game.Static import Enumerations as enums


class QuizScreen(BaseScreen):

    def __init__(self):
        self.noQuestion: int = None
        self.questionNo: int = None
        self.cheatMode: bool = None
        self.answerOption: enums.OptionType = None
        self.selectOption: enums.OptionType = None
        self.nextScreen: enums.ScreenType = None
        self.correctAns: bool = None
        self.flag: bool = None


    def Initialize(self) -> None:
        super().InitScreenText()


    def LoadContent(self) -> None:
        super().LoadContent()
        self.cheatMode = MyGame.Manager.QuestionManager.GetCheatMode()

        self.noQuestion = MyGame.Manager.QuestionManager.NumberQuestion
        self.questionNo = self.__getQuestionNumber()

        self.answerOption = self.__getAnswerOption()
        self.nextScreen = None
        self.correctAns = False
        self.flag = False


    def Update(self, deltaTime: int) -> ScreenType | None:
        if self.flag:
            super().BlockOnSoundFX()
            MyGame.Manager.QuestionManager.Increment()
            self.questionNo = self.__getQuestionNumber()

            qNo: int = self.questionNo + 1
            if qNo > self.noQuestion:
                if MyGame.Manager.SoundManager.SoundEnable:
                    # Slight pause before transition to Game Over
                    time.sleep(1)
                return ScreenType.Over

            return ScreenType.Play

        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            actor: bool = MyGame.Manager.InputManager.Character()
            if actor:
                return ScreenType.Score

            self.selectOption = MyGame.Manager.InputManager.GetOptionType()
            if self.selectOption != enums.OptionType.Invalid:
                self.correctAns = self.selectOption == self.answerOption
                if self.correctAns:
                    MyGame.Manager.ScoreManager.Increment()
                    MyGame.Manager.SoundManager.PlayRightSound()
                else:
                    MyGame.Manager.SoundManager.PlayWrongSound()

                self.flag = True

        return None


    def Draw(self) -> None:
        #  Draw all text first.
        super().DrawScreenText()
        MyGame.Manager.QuestionManager.DrawQuestion(self.questionNo)
        MyGame.Manager.QuestionManager.DrawQuizDiffText()
        MyGame.Manager.QuestionManager.DrawQuestionNumber()
        MyGame.Manager.QuestionManager.DrawQuestionTotal()
        MyGame.Manager.ScoreManager.DrawScore()

        #  Draw all images next.
        MyGame.Manager.ImageManager.DrawHeader()
        MyGame.Manager.ImageManager.DrawCurrActor()
        MyGame.Manager.SoundManager.DrawVolumeIcon()

        if self.cheatMode:
            MyGame.Manager.SpriteManager.DrawSelect(self.answerOption)
        else:
            MyGame.Manager.SpriteManager.DrawSelectAll()

        if self.flag:
            if self.correctAns:
                MyGame.Manager.SpriteManager.DrawRight(self.selectOption)
            else:
                MyGame.Manager.SpriteManager.DrawWrong(self.selectOption)


    def __getQuestionNumber(self) -> int:
        return MyGame.Manager.QuestionManager.QuestionNumber

    def __getAnswerOption(self) -> int:
        return MyGame.Manager.QuestionManager.CorrectOptionType
