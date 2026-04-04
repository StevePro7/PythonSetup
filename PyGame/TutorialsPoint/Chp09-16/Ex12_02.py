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
    screen.fill(white)
    screen.blit(img, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = x - 1
            if event.key == K_RIGHT:
                x = x + 1
            if event.key == K_UP:
                y = y - 1
            if event.key == K_DOWN:
                y = y + 1

    screen.blit(img, (x, y))
    pygame.display.update()
