import pygame
import sys

pygame.init()

# Window (your 640x480 setup)
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sprite Sheet Example")

# Internal SMS-like surface
sms_surface = pygame.Surface((640, 480))

clock = pygame.time.Clock()

# --- Load full sprite sheet ---
spritesheet = pygame.image.load("Sprites.bmp").convert()

# --- Function to get one 32x32 sprite ---
def get_spriteX(sheet, col, row, width=32, height=32):
    # Calculate position in sheet
    x = col * width
    y = row * height

    # Create a new surface
    sprite = pygame.Surface((width, height)).convert()

    # Copy that portion
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite


def get_sprite(sheet, col, row, width=32, height=32):
    rect = pygame.Rect(col * width, row * height, width, height)
    return sheet.subsurface(rect)


# Example: get sprite at column 1, row 2
sprite = get_sprite(spritesheet, col=0, row=1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sms_surface.fill((0, 0, 0))

    # Draw sprite at SMS coordinates (like tiles)
    sms_surface.blit(sprite, (50, 50))

    # Scale to window
    scaled = pygame.transform.scale(sms_surface, (640, 480))
    window.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()