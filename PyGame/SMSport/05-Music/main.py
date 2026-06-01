import pygame
import sys

pygame.mixer.init()
pygame.init()

#pygame.mixer.music.load("happymusic.mp3")
pygame.mixer.music.load("titlemusic.mp3")
pygame.mixer.music.play()

pygame.display.set_caption("Music Example")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.quit()