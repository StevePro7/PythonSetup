from Game.MyGame import MyGame
from Game.Screens.BaseScreen import BaseScreen
from Game.Static.Enumerations import ScreenType
from Game.Static import Enumerations as enums


class OverScreen(BaseScreen):

    def __init__(self):
        self.totalText: str = None
        self.solveText: str = None
        self.visorText: str = None
        self.solveValu: int = None
        self.visorValu: int = None

    def Initialize(self) -> None:
        super().InitScreenText()
        self.overDelay = MyGame.Manager.ConfigManager.ConfigData.OverDelay


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
        MyGame.Manager.SoundManager.PlayMusic(enums.MusicType.HappyMusic)


    def Update(self, deltaTime: int) -> ScreenType | None:
        icon: bool = super().UpdateVolumeIcon()
        if not icon:
            actor: bool = MyGame.Manager.InputManager.Character()
            back: bool = MyGame.Manager.InputManager.Back()
            if actor or back:
                MyGame.Manager.SoundManager.StopMusic()
                return ScreenType.Init

        super().UpdateTimer(deltaTime)
        complete: bool = self.Timer > self.overDelay

        playing: bool = MyGame.Manager.SoundManager.IsMusicPlaying()
        if complete and not playing:
            MyGame.Manager.SoundManager.StopMusic()
            return ScreenType.Init

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

