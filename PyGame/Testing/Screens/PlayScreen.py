from MyGame import MyGame
from Screens.BaseScreen import BaseScreen
from enumerations import ScreenType
import enumerations


class PlayScreen(BaseScreen):

    def __init__(self):
        self.questionNo: int = None
        self.cheatMode: bool = None
        self.optionType: enumerations.OptionType = None


    def Initialize(self) -> None:
        super().InitScreenText()


    def LoadContent(self) -> None:
        MyGame.Manager.ImageManager.GenerateNextActor()
        self.cheatMode = MyGame.Manager.QuestionManager.GetCheatMode()

        self.questionNo = MyGame.Manager.QuestionManager.QuestionNumber
        MyGame.Manager.QuestionManager.PlayQuestion(self.questionNo)
        if MyGame.Manager.ConfigManager.ConfigData.RandomAnswers:
            MyGame.Manager.QuestionManager.RandomizeAnswerList(self.questionNo)

        # Correct option is now set!
        self.optionType =  MyGame.Manager.QuestionManager.CorrectOptionType


    def Update(self, deltaTime: int) -> ScreenType | None:
        super().UpdateVolumeIcon()
        return ScreenType.Quiz


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
            MyGame.Manager.SpriteManager.DrawSelect(self.optionType)
        else:
            MyGame.Manager.SpriteManager.DrawSelectAll()
