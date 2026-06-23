from dataclasses import dataclass
from Game.Static.Enumerations import ScreenType, OptionType, DifficultyType


@dataclass(frozen=True)
class ConfigData:
    FPS: int
    ScreenType: ScreenType
    Debugging: bool
    OptionType: OptionType
    DifficultyType: DifficultyType
    SplashDelay: int
    TitleDelay: int
    OptionDelay: int
    DotsDelay: int
    OverDelay: int
    FlashTitle: bool
    SoundEnable: bool
    CheatMode: bool
    RandomQuestions: bool
    RandomAnswers: bool
    Fullscreen: bool
