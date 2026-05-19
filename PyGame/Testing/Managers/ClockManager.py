import pygame


class ClockManager:
    def Initialize(self):
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps = 100

    def Update(self) -> int:
        deltaTime: int = self.clock.tick(self.fps)
        return deltaTime
