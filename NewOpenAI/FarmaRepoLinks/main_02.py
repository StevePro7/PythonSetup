from enum import Enum
from typing import Dict

class Environments(Enum):
    CLASSIC_CONTROL = 1
    BOX_2D          = 2
    TOY_TEXT        = 3
    MUJO_CO         = 4
    ATARI           = 5


games: Dict[int, str] = {
    Environments.CLASSIC_CONTROL.value: "ClassicControl",
    Environments.BOX_2D.value:          "Box2D",
    Environments.TOY_TEXT.value:        "ToyText",
    Environments.MUJO_CO.value:         "MuJoCo",
    Environments.ATARI.value:           "Atari"
}

key: int = Environments.BOX_2D.value
#key: int = Environments.CLASSIC_CONTROL.value
#print(games)
dat: str = games[key]
print(dat)
# Accessing enum members
# print(Environments.CLASSIC_CONTROL)
# print(Environments.BOX_2D)
# print(Environments.TOY_TEXT)
# print(Environments.MUJO_CO)
# print(Environments.ATARI)


