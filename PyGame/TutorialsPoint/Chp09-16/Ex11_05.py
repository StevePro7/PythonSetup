import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

done = False
white=(255,255,255)

text: str = ""

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            text = text + event.unicode

        font = pygame.font.SysFont("Arial", 36)
        img = font.render(text, True, white)
        rect = img.get_rect()
        cursor = pygame.Rect(rect.topright, (3, rect.height))
        img = font.render(text, True, white)
        rect.size = img.get_size()
        cursor.topleft = rect.topright
        screen.blit(img, (20 - img.get_width() // 2, 10 - img.get_height() // 2))

    pygame.display.update()