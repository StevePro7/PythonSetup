import pygame
import sys

pygame.init()
canvas = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            key = pygame.key.name(event.key)
            print(key, "Key is pressed")
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print(key, "Key is released")
