import pygame

from MyGame import MyGame


class KeyboardInput:
    def __init__(self):
        self.curr_keys = None
        self.prev_keys = None


    def Update(self, deltaTime: int):
        # snapshot previous
        self.prev_keys = self.curr_keys
        self.curr_keys = pygame.key.get_pressed()


    def KeyPress(self, key: int) -> bool:
        return self.curr_keys[key]


    def KeyHold(self, key: int) -> bool:
        if not self.prev_keys:
            return False

        return self.curr_keys[key] and not self.prev_keys[key]
