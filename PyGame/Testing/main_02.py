import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))

print("Window created")
print("sleep")
time.sleep(1)
print("red")
screen.fill((255, 0, 0))
pygame.display.flip()
print("flip")
print("Frame drawn")

time.sleep(4)