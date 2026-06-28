import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Splash")
sms_surface = pygame.Surface((640, 480))

splash = pygame.image.load("StevePro.bmp").convert()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dest: tuple[float, float] = ((640 - splash.get_width()) / 2, (480 - splash.get_height()) / 2)
    sms_surface.blit(splash, dest=dest)

    screen.fill((0, 0, 0))
    scaled = pygame.transform.scale(sms_surface, (640, 480))
    screen.blit(scaled, (0, 0))

    pygame.display.flip()

pygame.quit()