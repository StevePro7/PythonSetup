import pygame
import sys

# Initialize pygame
pygame.init()

# Create a window (SMS resolution is 640x480)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

# Your palette color: RGB(3,3,3) in SMS is low intensity.
# SMS uses 0–3 per channel, pygame uses 0–255, so scale it:
def sms_rgb(r, g, b):
    return (r * 85, g * 85, b * 85)  # 0–3 → 0–255

color0 = sms_rgb(3, 3, 3)

clock = pygame.time.Clock()

# Equivalent to SMS_displayOn() + main loop
running = True
while running:
    # Handle window events (important in pygame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Equivalent to having a background color
    screen.fill(color0)

    # Equivalent to end-of-frame / VBlank sync
    pygame.display.flip()
    clock.tick(60)  # ~60 FPS, similar to VBlank timing

pygame.quit()
sys.exit()