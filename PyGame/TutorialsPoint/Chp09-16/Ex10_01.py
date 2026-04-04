import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
img = pygame.image.load("SteveProXNA.jpg")
done: bool = False

bg = (127, 127, 127)
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.display.set_caption("Hello World")

while not done:
    for event in pygame.event.get():
        screen.fill(bg)
        rect = img.get_rect()
        rect.center = 44, 44
        screen.blit(img, rect)
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.circle(screen, red, (200, 150), 60, 2)
        pygame.draw.circle(screen, green, (200, 150), 80, 2)
        pygame.draw.circle(screen, blue, (200, 150), 100, 2)
    pygame.display.update()
    #pygame.image.save("circles.png")
