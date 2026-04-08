import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Move image with mouse")
img1 = pygame.image.load("SteveProXNA.jpg")
done = False

bg = (127, 127, 127)

while not done:
    for event in pygame.event.get():
        screen.fill(bg)

        if event.type == pygame.QUIT:
            done = True

        if event.type == MOUSEMOTION:
            mouse = event.pos
            x = mouse[0] - 200
            y = mouse[1] - 150
            d = math.sqrt(x ** 2 + y ** 2)
            angle = math.degrees(-math.atan2(y, x))
            scale = abs(5 * d / 400)
            img2 = pygame.transform.rotozoom(img1, angle, scale)
            rect = img2.get_rect()
            rect.center =  (200, 150)
            screen.blit(img2, rect)

    pygame.display.update()

pygame.quit()