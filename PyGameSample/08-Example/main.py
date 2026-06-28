import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Audio")

font = pygame.font.Font(None, 48)  # Built-in default font

def render_text(text, color=(255, 255, 255)):
    return font.render(text, False, color)

text1 = render_text("Hello Audio!" )
text2 = render_text("Press Left - sound #1")
text3 = render_text("Press Right - sound #2")
text4 = render_text("Press Up - play music")
text5 = render_text("Press Down - stop music")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text1, (220, 140))
    screen.blit(text2, (160, 180))
    screen.blit(text3, (160, 220))
    screen.blit(text4, (160, 260))
    screen.blit(text5, (160, 300))

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     space = font.render("Space pressed!!", True, (255, 255, 255))
    #     screen.blit(space, (200, 260))

    pygame.display.flip()

pygame.quit()