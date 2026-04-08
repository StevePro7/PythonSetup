import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Draw rect with mouse")
screen.fill((127,127,127))
x=0
y=0
w=0
h=0
drawmode=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            drawmode = True
        if event.type == MOUSEBUTTONUP:
            x1,y1 = pygame.mouse.get_pos()
            w=x1-x
            h=y1-y
            drawmode= False
    rect = pygame.Rect(x,y,w,h)
    if drawmode == False:
        pygame.draw.rect(screen, (255,0,0), rect)

    pygame.display.flip()
pygame.quit()