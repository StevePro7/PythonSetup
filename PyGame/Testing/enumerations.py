from enum import Enum, auto

class ZeroBasedEnum(Enum):
    @staticmethod
    # Ensure that all enums zero-based index.
    def _generate_next_value_(name, start, count, last_values):
        return count


class ScreenType(ZeroBasedEnum):
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


class SpriteType(ZeroBasedEnum):
    Select = auto()
    Right = auto()
    Wrong = auto()
    LeftArrow = auto()
    RightArrow = auto()
    VolumeOn = auto()
    VolumeOff = auto()
    White = auto()


class MusicType(ZeroBasedEnum):
    HappyMusic = auto()
    TitleMusic = auto()


class SoundType(ZeroBasedEnum):
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
