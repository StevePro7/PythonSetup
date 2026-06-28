import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Music")

font = pygame.font.Font(None, 48)  # Built-in default font
pygame.mixer.music.load("music.wav")

def render_text(text, color=(255, 255, 255)):
    return font.render(text, False, color)

text1 = render_text("Hello Music!" )
text2 = render_text("Press Up - play music")
text3 = render_text("Press Down - stop music")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text1, (220, 140))
    screen.blit(text2, (160, 180))
    screen.blit(text3, (160, 220))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        space = font.render("Space pressed!!", True, (255, 255, 255))
        screen.blit(space, (200, 260))
        pygame.mixer.music.play()
    if keys[pygame.K_DOWN]:
        space = font.render("Space pressed??", True, (255, 255, 255))
        screen.blit(space, (200, 260))
        pygame.mixer.music.stop()

    pygame.display.flip()

pygame.quit()