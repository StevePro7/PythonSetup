from dataclasses import dataclass


@dataclass
class ConfigData:
    FPS: int = 50
    Width: int = 640
    Height: int = 480
    Fullscreen: bool = False
