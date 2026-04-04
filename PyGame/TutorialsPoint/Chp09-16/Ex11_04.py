import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

done = False
white=(255,255,255)

font1 = pygame.font.SysFont("emulogic.ttf", 72)
pygame.display.set_caption("Hello World")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    txtsurf = font1.render("Hello, World", True, white)
    screen.blit(txtsurf, (200, 100))
    pygame.display.update()