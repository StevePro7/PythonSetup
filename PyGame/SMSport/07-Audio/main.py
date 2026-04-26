import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)  # loop forever

# Load sound effects
cheat_sfx = pygame.mixer.Sound("cheat.wav")
ready_sfx = pygame.mixer.Sound("ready.wav")
right_sfx = pygame.mixer.Sound("right.wav")
wrong_sfx = pygame.mixer.Sound("wrong.wav")

pygame.display.set_caption("SFX example")
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("SFX Test")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cheat_sfx.play()
                print("CHEAT SFX")
            elif event.key == pygame.K_a:
                right_sfx.play()
                print("RIGHT SFX")
            elif event.key == pygame.K_s:
                wrong_sfx.play()
                print("WRONG SFX")
            elif event.key == pygame.K_z:
                ready_sfx.play()
                print("READY SFX")
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()