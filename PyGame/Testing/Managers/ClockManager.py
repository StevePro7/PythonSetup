import pygame

from MyGame import MyGame


class ClockManager:
    def Initialize(self):
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps = MyGame.Manager.ConfigManager.ConfigData.FPS

    def Update(self) -> int:
        deltaTime: int = self.clock.tick(self.fps)
        return deltaTime
