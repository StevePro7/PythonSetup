from dataclasses import dataclass
from enumerations import ScreenType, OptionType, DifficultyType


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
    BlankSplash: bool
    FlashTitle: bool
    MusicEnable: bool   # adriana
    SoundEnable: bool
    CheatMode: bool
    RandomQuestions: bool
    RandomAnswers: bool
    Fullscreen: bool
