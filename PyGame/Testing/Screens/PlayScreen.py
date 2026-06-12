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
            MyGame.Manager.QuestionManager.RandomizeAnswerPosn()

        # Correct option is now set!
        self.optionType =  MyGame.Manager.QuestionManager.CorrectOptionType


    def Update(self, deltaTime: int) -> ScreenType | None:
        return None


    def Draw(self) -> None:
        super().DrawScreenText()
        MyGame.Manager.QuestionManager.DrawQuestion(self.questionNo)
