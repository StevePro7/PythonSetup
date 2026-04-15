import pygame
import sys
from pygame.locals import *

pygame.init()
#pygame.mouse.set_cursor(pygame.cursors.broken_x)
cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_WAITARROW)
pygame.mouse.set_cursor(cursor)
canvas = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cursor")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(1)
