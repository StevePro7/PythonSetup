from dataclasses import dataclass
from enumerations import ScreenType, OptionType, DifficultyType


@dataclass(frozen=True)
class ConfigData:
    FPS: int
    ScreenType: ScreenType
    OptionType: OptionType
    DifficultyType: DifficultyType
    SplashDelay: int
    MusicEnable: bool   # adriana
    SoundEnable: bool
    Fullscreen: bool
