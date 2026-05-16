import os
import pygame
import sys

class Game:
    def __init__(self):
        self.fps = 50
        self.running = True

    def update(self, dt):
        print(dt)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


if __name__ == "__main__":
    print("start")
    pygame.init()
    print("hi")
    game = Game()
    game.loop()
    print('bye')
    pygame.quit()
