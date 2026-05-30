import pygame

class PyGameManager:
    def Initialize(self):
        pygame.init()

    def Quit(self):
        pygame.quit()

    def Present(self):
        # Swaps the entire back buffer to the screen
        pygame.display.flip()