import pygame
import sys

pygame.init()

# Window
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Internal "SMS screen"
sms_surface = pygame.Surface((256, 192))

# Load sprite sheet
sheet = SpriteSheet("StevePro.bmp")

# Extract a 32x32 tile (col=1,row=2)
tile_image = sheet.image_at(1, 2)

# Create sprite object
sprite = GameSprite(tile_image, x=50, y=50)

# Sprite group (important in Pygame architecture)
sprites = pygame.sprite.Group()
sprites.add(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sms_surface.fill((0, 0, 0))

    # Update all sprites
    sprites.update()

    # Draw all sprites
    sprites.draw(sms_surface)

    # Scale to window (SMS → PC)
    scaled = pygame.transform.scale(sms_surface, (640, 480))
    window.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()