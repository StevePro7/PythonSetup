import random
import time


class RandomManager:
    def __init__(self):
        self._random = None


    def Initialize(self, seed: int = None):
        if seed is None:
            seed = int(time.time_ns()) & 0xFFFF

        self._random = random.Random(seed)

    def Next(self, *args) -> int:
        if len(args) == 1:
            max_val: int = args[0]
            return self._random.randrange(max_val)
        elif len(args) == 2:
            min_val: int = args[0]
            max_val: int = args[1]
            return self._random.randrange(min_val, max_val)
        else:
            raise TypeError("next() expects 1 or 2 arguments")
