import pygame
import sys

class Game:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Simpsons Trivia (PyGame)")

        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = None  # active screen

    def set_scene(self, scene):
        self.scene = scene

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.scene:
                self.scene.handle_event(event)

    def update(self):
        if self.scene:
            self.scene.update()

    def draw(self):
        if self.scene:
            self.scene.draw(self.screen)
        pygame.display.flip()