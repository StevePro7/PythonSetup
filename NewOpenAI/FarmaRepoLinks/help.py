from enum import Enum
from typing import Dict


class Environments(Enum):
    CLASSIC_CONTROL = 1
    BOX_2D          = 2
    TOY_TEXT        = 3
    MUJO_CO         = 4
    ATARI           = 5

Folders: Dict[int, str] = {
    Environments.CLASSIC_CONTROL.value: "ClassicControl",
    Environments.BOX_2D.value:          "Box2D",
    Environments.TOY_TEXT.value:        "ToyText",
    Environments.MUJO_CO.value:         "MuJoCo",
    Environments.ATARI.value:           "Atari"
}
