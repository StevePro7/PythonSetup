import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello PyGame")

font = pygame.font.Font(None, 48)  # Built-in default font
text = font.render("Hello PyGame!", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, (220, 220))
    pygame.display.flip()

pygame.quit()