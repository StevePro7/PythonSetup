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
    Unknown = auto()


class DifficultyType(ZeroBasedEnum):
    Easy = auto()
    Norm = auto()
    Hard = auto()
    Argh = auto()


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


class SpriteType(ZeroBasedEnum):
    Select = auto()
    Right = auto()
    Wrong = auto()
    LeftArrow = auto()
    RightArrow = auto()
    VolumeOn = auto()
    VolumeOff = auto()
    White = auto()


class OptionType(ZeroBasedEnum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    Invalid = auto()


class MouseType(ZeroBasedEnum):
    Left = auto()
    Middle = auto()
    Right = auto()


class ActorType(ZeroBasedEnum):
    Bart1 = auto()
    Bart2 = auto()
    Comic = auto()
    Drhibbert = auto()
    Drnick = auto()
    Flanders = auto()
    Grampa1 = auto()
    Homer1 = auto()
    Homer2 = auto()
    Homer3 = auto()
    Lisa1 = auto()
    Lisa2 = auto()
    Maggie = auto()
    Marge0 = auto()
    Skinner = auto()
    Troy = auto()
