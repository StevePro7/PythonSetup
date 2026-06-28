import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Sound")

font = pygame.font.Font(None, 48)  # Built-in default font

text1 = font.render("Hello Sound!", True, (255, 255, 255))
text2 = font.render("Press Left - sound #1", True, (255, 255, 255))
text3 = font.render("Press Right - sound #2", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text1, (220, 220))
    screen.blit(text2, (160, 260))
    screen.blit(text3, (160, 300))

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     space = font.render("Space pressed!!", True, (255, 255, 255))
    #     screen.blit(space, (200, 260))

    pygame.display.flip()

pygame.quit()