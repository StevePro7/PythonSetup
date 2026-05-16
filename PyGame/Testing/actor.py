import pygame

# -----------------------------
# Constants (match your XNA layout)
# -----------------------------
IMAGE_WIDE = 240
IMAGE_HIGH = 320

SCREEN_W = 640
SCREEN_H = 480

MAX_ACTOR_INDEX = 15
MIN_ACTOR_INDEX = 0


class ActorViewer:
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet

        self.actor_rects = self.populate_actor_rects()

        # same idea as actorVect in XNA
        self.actor_pos = (
            SCREEN_W - IMAGE_WIDE - 50,
            SCREEN_H - IMAGE_HIGH
        )

    # -----------------------------
    # Actor rects (same mapping as your C#)
    # -----------------------------
    def populate_actor_rects(self):
        rects = [None] * 16

        rects[0] = self.get_rect(0, 2)
        rects[1] = self.get_rect(0, 3)
        rects[2] = self.get_rect(1, 2)
        rects[3] = self.get_rect(1, 3)

        rects[4] = self.get_rect(2, 0)
        rects[5] = self.get_rect(2, 1)
        rects[6] = self.get_rect(2, 2)
        rects[7] = self.get_rect(2, 3)

        rects[8] = self.get_rect(3, 0)
        rects[9] = self.get_rect(3, 1)
        rects[10] = self.get_rect(3, 2)
        rects[11] = self.get_rect(3, 3)

        rects[12] = self.get_rect(4, 0)
        rects[13] = self.get_rect(4, 1)
        rects[14] = self.get_rect(4, 2)
        rects[15] = self.get_rect(4, 3)

        return rects

    def get_rect(self, x, y):
        return pygame.Rect(
            x * IMAGE_WIDE,
            y * IMAGE_HIGH,
            IMAGE_WIDE,
            IMAGE_HIGH
        )

    # -----------------------------
    # THIS is your draw_actor()
    # -----------------------------
    def draw_actor(self, screen, index):
        sprite = self.spritesheet.subsurface(self.actor_rects[index])
        screen.blit(sprite, self.actor_pos)


# -----------------------------
# Main Hello World
# -----------------------------
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Actor Draw Hello World")

    clock = pygame.time.Clock()

    spritesheet = pygame.image.load("Spritesheet.png").convert_alpha()

    viewer = ActorViewer(spritesheet)

    # 👉 CHANGE THIS VALUE to test different actors
    actor_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    actor_index = max(MIN_ACTOR_INDEX, actor_index - 1)

                if event.key == pygame.K_RIGHT:
                    actor_index = min(MAX_ACTOR_INDEX, actor_index + 1)

        screen.fill((255, 255, 255))

        # draw actor (XNA equivalent call)
        viewer.draw_actor(screen, actor_index)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()