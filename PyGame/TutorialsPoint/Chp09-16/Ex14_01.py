import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Image")
img = pygame.image.load("SteveProXNA.jpg")
x: int = 200
y: int = 150
white=(255,255,255)

while True:
    mx, my = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(img, (mx - 44, my - 44))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
