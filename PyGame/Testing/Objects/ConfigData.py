from dataclasses import dataclass
from enumerations import ScreenType


@dataclass(frozen=True)
class ConfigData:
    FPS: int
    ScreenType: ScreenType
    MusicEnable: bool   # adriana
    SoundEnable: bool
    Fullscreen: bool
