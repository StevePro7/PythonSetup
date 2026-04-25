import pygame
import sys

pygame.init()

# --- Resolution setup ---
#SMS_WIDTH = 256
#SMS_HEIGHT = 192

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Emulogic Font Example")

# Internal SMS surface
sms_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

# --- Load Emulogic font ---
# 20px ≈ one 8x8 tile scaled to 640x480
FONT_SIZE = 20

font = pygame.font.Font("emulogic.ttf", FONT_SIZE)

# Disable smoothing (important for pixel fonts)
def render_text(text, color=(255, 255, 255)):
    return font.render(text, False, color)  # False = no anti-aliasing

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear SMS surface
    sms_surface.fill((0, 0, 0))

    # Render text (tile-like positioning)
    text_surface = render_text("HELLO SMS PORT")

    # Position in "tile space"
    # e.g. tile (5,5) = 5*8,5*8 in SMS coords
    tile_x = 0
    tile_y = 0
    sms_surface.blit(text_surface, (tile_x * 8, tile_y * 8))

    # Scale up to window
    scaled = pygame.transform.scale(sms_surface, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()