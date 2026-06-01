from enum import Enum, auto

class ScreenType(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count

    Splash = auto()     # 0
    Init = auto()
    Title = auto()
    Diff = auto()
    Long = auto()
    Ready = auto()
    Play = auto()
    Quiz = auto()
    Score = auto()
    Over = auto()
    Exit = auto()
    Test = auto()       # 11


class MusicType(Enum):
    HappyMusic = auto()
    TitleMusic = auto()


class SoundType(Enum):
    Right_01 = auto()
    Right_02 = auto()
    Right_03 = auto()
    Right = auto()
    Wrong_01 = auto()
    Wrong_02 = auto()
    Wrong_03 = auto()
    Wrong = auto()
    Cheat = auto()
    Ready = auto()
