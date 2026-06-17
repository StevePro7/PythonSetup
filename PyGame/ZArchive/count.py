import pygame

SCREEN_W = 640
SCREEN_H = 480

MIN_INDEX = 0
MAX_INDEX = 15


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Hold to Move Actor Index")

    clock = pygame.time.Clock()

    actor_index = 0

    # speed control (how fast index changes while holding)
    hold_speed = 15  # frames per increment
    hold_counter = 0

    running = True
    while running:

        # -------------------------
        # events (still needed for quit)
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # -------------------------
        # continuous input (THIS is the key)
        # -------------------------
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            hold_counter += 1
            if hold_counter >= hold_speed:
                actor_index = min(MAX_INDEX, actor_index + 1)
                hold_counter = 0
        elif keys[pygame.K_LEFT]:
            hold_counter += 1
            if hold_counter >= hold_speed:
                actor_index = max(MIN_INDEX, actor_index - 1)
                hold_counter = 0
        else:
            # reset when no key pressed
            hold_counter = 0

        # -------------------------
        # render
        # -------------------------
        screen.fill((25, 25, 25))

        # debug display
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Actor Index: {actor_index}", True, (255, 255, 255))
        screen.blit(text, (50, 200))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()