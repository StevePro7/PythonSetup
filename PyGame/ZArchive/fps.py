import os
import pygame
import sys

class Game:
    def __init__(self):
        self.fps = 100
        self.running = True
        self.clock = pygame.time.Clock()

    def update(self, dt):
        print(dt)

    def loop(self):
        dt = 0
        self.clock.tick(self.fps)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # deltaTime in milliseconds.
            dt = self.clock.tick(self.fps)
            self.update(dt)


if __name__ == "__main__":
    print("start")
    pygame.init()
    print("hi")
    game = Game()
    game.loop()
    print('bye')
    pygame.quit()
