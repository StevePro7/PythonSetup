import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Text")
sms_surface = pygame.Surface((640, 480))

font = pygame.font.Font("emulogic.ttf", 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sms_surface.fill((0, 0, 0))
    text_surface = font.render("Hello Text!", False, (255, 255, 255))
    sms_surface.blit(text_surface, (0, 0))
    scaled = pygame.transform.scale(sms_surface, (640, 480))
    screen.blit(scaled, (220, 220))

    pygame.display.flip()

pygame.quit()