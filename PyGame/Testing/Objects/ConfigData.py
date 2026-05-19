from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigData:
    FPS: int
    Width: int
    Height: int
    Fullscreen: bool


# @dataclass(frozen=True)
# class ConfigData:
#     FPS: int = 50
#     Width: int = 640
#     Height: int = 480
#     Fullscreen: bool = False