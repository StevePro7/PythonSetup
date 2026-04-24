import pygame
import sys

pygame.init()

# Internal SMS resolution
# SMS_WIDTH = 256
# SMS_HEIGHT = 192

# Window size
SCREEN_WIDE = 640
SCREEN_HIGH = 480

window = pygame.display.set_mode((SCREEN_WIDE, SCREEN_HIGH))
pygame.display.set_caption("Splash Screen")

# Create a low-res surface (like SMS VRAM output)
sms_surface = pygame.Surface((SCREEN_WIDE, SCREEN_HIGH))

clock = pygame.time.Clock()

# Load image
splash = pygame.image.load("StevePro.bmp").convert()


# Ensure it matches SMS resolution
#splash = pygame.transform.scale(splash, (SMS_WIDTH, SMS_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw to SMS surface
    dest: tuple[float, float] = ((SCREEN_WIDE - splash.get_width()) / 2, (SCREEN_HIGH - splash.get_height()) / 2)
    sms_surface.blit(splash, dest=dest)

    # Scale up to window (choose one)

    # Option 1: smooth (slightly blurry)
    #scaled = pygame.transform.smoothscale(sms_surface, (SCREEN_WIDE, SCREEN_HIGH))

    # Option 2 (better for retro): pixel-perfect scaling
    scaled = pygame.transform.scale(sms_surface, (SCREEN_WIDE, SCREEN_HIGH))

    window.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()