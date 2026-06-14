from MyGame import MyGame

# adriana
class ResolutionManager:
    def __init__(self):
        self.scale: float = 1.0
        self.offset: tuple = (0, 0)

        self.game_size: tuple = (0, 0)          # e.g. (640, 480)
        self.screen_size: tuple = (0, 0)        # fullscreen size


    def Configure(self, game_size: tuple, screen_size: tuple, scale: float, offset: tuple):
        self.game_size = game_size
        self.screen_size = screen_size
        self.scale = scale
        self.offset = offset


    def ScreenToGame(self, pos: tuple[int, int]) -> tuple[int, int]:
        x, y = pos

        # Remove offset (centering)
        x -= self.offset[0]
        y -= self.offset[1]

        if x < 0 or y < 0:
            return (-1, -1)

        max_w = int(self.game_size[0] * self.scale)
        max_h = int(self.game_size[1] * self.scale)

        if x > max_w or y > max_h:
            return (-1, -1)

        return (int(x / self.scale), int(y / self.scale))


    #  Game (640x480) to Screen (fullscreen)
    def GameToScreen(self, pos: tuple[int, int]) -> tuple[int, int]:
        x, y = pos

        x = int(x * self.scale + self.offset[0])
        y = int(x * self.scale + self.offset[1])

        return (x, y)


    # Check if a screen-space coordinate is inside the viewport
    def IsInsideGame(self, pos: tuple[int, int]) -> bool:
        x, y = pos

        x -= self.offset[0]
        y -= self.offset[1]

        if x < 0 or y < 0:
            return False

        max_w = int(self.game_size[0] * self.scale)
        max_h = int(self.game_size[1] * self.scale)

        return x <= max_w and y <= max_h
