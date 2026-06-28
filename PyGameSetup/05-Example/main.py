import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Input")

font = pygame.font.Font(None, 48)  # Built-in default font
text = font.render("Hello Input - Press space...", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, (100, 220))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        space = font.render("Space pressed!!", True, (255, 255, 255))
        screen.blit(space, (200, 260))

    pygame.display.flip()

pygame.quit()