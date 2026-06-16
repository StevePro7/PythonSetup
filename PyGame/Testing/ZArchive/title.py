import pygame
import math

# -----------------------------
# Minimal constants (match your setup)
# -----------------------------
IMAGE_WIDE = 240
IMAGE_HIGH = 320

TITLE_RECT = pygame.Rect(0, 0, 2 * IMAGE_WIDE, 2 * IMAGE_HIGH)
TITLE_VECT = (2 * IMAGE_WIDE, 0)

IMAGE_ROTATE = math.radians(90)


# -----------------------------
# Simple draw function (XNA-style title)
# -----------------------------
def draw_title(screen, spritesheet):
    # extract region
    image = spritesheet.subsurface(TITLE_RECT)

    # rotate like XNA (270 degrees)
    rotated = pygame.transform.rotate(image, math.degrees(IMAGE_ROTATE))

    # position (same idea as your Vector2 zeroPosn)
    pos = (0, 0)

    screen.blit(rotated, pos)


# -----------------------------
# Main program
# -----------------------------
def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Simpsons Trivia")

    clock = pygame.time.Clock()

    # load spritesheet
    spritesheet = pygame.image.load("Spritesheet.png").convert_alpha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear screen
        screen.fill((255, 255, 255))

        # draw title from spritesheet
        draw_title(screen, spritesheet)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()