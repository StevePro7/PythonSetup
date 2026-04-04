import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

done = False
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg = (127,127,127)

font = pygame.font.SysFont("Arial", 36)
pygame.display.set_caption("Hello World")

while not done:
    for event in pygame.event.get():
        screen.fill(bg)

        if event.type == pygame.QUIT:
            done = True

    txtsurf = font.render("Hello, World", True, white)
    screen.blit(txtsurf, (200, 100))
    pygame.display.update()