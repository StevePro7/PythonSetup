import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
white = (255, 255, 255, 0)
font = pygame.font.SysFont("Arial", 36)


pygame.display.set_caption("Hello World")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    txtsurf = font.render("Hello, World", True, white)
    screen.blit(txtsurf, (200, 100))
    pygame.display.update()