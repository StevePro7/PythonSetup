import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Image")
img = pygame.image.load("SteveProXNA.jpg")
x: int = 0
white=(255,255,255)

while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(img, (x, 100))
    x = x + 0.1
    if x > 560:
        x = x - 560

    pygame.display.update()
