class CoordinateMapper:
    def __init__(self):
        self.scale = 1.0
        self.offset = (0, 0)
        self.game_size = (0, 0)

    def Configure(self, scale, offset, game_size):
        self.scale = scale
        self.offset = offset
        self.game_size = game_size

    def ScreenToGame(self, pos):
        x, y = pos

        # Remove offset
        x -= self.offset[0]
        y -= self.offset[1]

        if x < 0 or y < 0:
            return (-1, -1)

        max_w = int(self.game_size[0] * self.scale)
        max_h = int(self.game_size[1] * self.scale)

        if x > max_w or y > max_h:
            return (-1, -1)

        return (int(x / self.scale), int(y / self.scale))
