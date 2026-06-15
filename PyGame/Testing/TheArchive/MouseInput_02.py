import pygame
from MyGame import MyGame


class MouseInput:
    def __init__(self):
        self.curr_buttons = None
        self.prev_buttons = None

        self.curr_x = 0
        self.curr_y = 0


    def Update(self, deltaTime: int):
        self.prev_buttons = self.curr_buttons

        self.curr_buttons = pygame.mouse.get_pressed()

        raw_x, raw_y = pygame.mouse.get_pos()

        self.curr_x, self.curr_y = MyGame.Manager.ResolutionManager.ScreenToGame(
            (raw_x, raw_y)
        )


    @property
    def CurrMouseX(self) -> int:
        return self.curr_x

    @property
    def CurrMouseY(self) -> int:
        return self.curr_y


    def ButtonDown(self, index=0) -> bool:
        # 0 = left, 1 = middle, 2 = right
        return self.curr_buttons[index]


    def ButtonHold(self, index=0) -> bool:
        if not self.prev_buttons:
            return False

        return self.curr_buttons[index] and not self.prev_buttons[index]


    def ButtonClick(self, index=0) -> bool:
        return self.ButtonHold(index)


    def MousePosition(self) -> (int, int):
        return (self.CurrMouseX, self.CurrMouseY)


    def IsInBounds(self) -> bool:
        return self.curr_x >= 0 and self.curr_y >= 0
