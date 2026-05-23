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
