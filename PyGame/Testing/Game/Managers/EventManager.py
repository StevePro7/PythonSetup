import pygame


class EventManager:

    def __init__(self):
        self.QuitRequested = False
        self.Events = []


    def ProcessEvents(self):
        self.Events.clear()
        for event in pygame.event.get():

            self.Events.append(event)
            if event.type == pygame.QUIT:
                self.QuitRequested = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.QuitRequested = True
