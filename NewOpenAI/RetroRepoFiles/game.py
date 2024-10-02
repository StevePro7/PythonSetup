from enum import Enum
from typing import Dict


class Environments(Enum):
    GENESIS = 1
    SMS     = 2

Folders: Dict[int, str] = {
    Environments.GENESIS:   "Genesis",
    Environments.SMS:       "Sms"
}
