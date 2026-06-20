import pygame
import os

# os.environ["SDL_VIDEODRIVER"] = "x11"
# os.environ["SDL_RENDER_DRIVER"] = "software"
# os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
# os.environ["SDL_OPENGL"] = "0"

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print("hello")
    screen.fill((0, 255, 0))
    pygame.display.update()