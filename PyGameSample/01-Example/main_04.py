import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello Sprites")
sms_surface = pygame.Surface((320, 240))

spritesheet = pygame.image.load("Sprites.bmp").convert()

def get_sprite(sheet, col, row, width=32, height=32):
    rect = pygame.Rect(col * width, row * height, width, height)
    return sheet.subsurface(rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sms_surface.fill((0, 0, 0))

    sprite1 = get_sprite(spritesheet, col=0, row=0)
    sprite2 = get_sprite(spritesheet, col=0, row=1)
    sms_surface.blit(sprite1, (64, 64))
    sms_surface.blit(sprite2, (128, 64))

    scaled = pygame.transform.scale(sms_surface, (640, 480))
    screen.blit(scaled, (0, 0))

    pygame.display.flip()

pygame.quit()