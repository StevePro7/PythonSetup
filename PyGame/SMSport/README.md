25-Apr-2026

scrolling
Just say:
"build me a scrolling demo with parallax + SFX"
and I’ll wire everything together.


Yes — Pygame absolutely supports Xbox 360 controllers 🎮
On Windows especially, they usually “just work” because they use XInput.


import pygame

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
print(f"Connected controllers: {joystick_count}")

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Controller name:", joystick.get_name())
	
	
	
for event in pygame.event.get():
    if event.type == pygame.JOYBUTTONDOWN:
        print("Button pressed:", event.button)
		
		
if event.button == 0:
    print("A pressed")
	
	
if event.type == pygame.JOYAXISMOTION:
    print("Axis", event.axis, "value:", event.value)
	
	
if event.type == pygame.JOYHATMOTION:
    print("D-pad:", event.value)
	
	
	
	
Full Pygame Demo (Scrolling + Parallax + SFX)
import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.joystick.init()

# ----------------------------
# Setup
# ----------------------------
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling + Parallax + SFX Demo")

clock = pygame.time.Clock()

# ----------------------------
# Load SFX
# ----------------------------
right_sfx = pygame.mixer.Sound("right.wav")
wrong_sfx = pygame.mixer.Sound("wrong.wav")

# ----------------------------
# Controller setup (if present)
# ----------------------------
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Controller connected:", joystick.get_name())

# ----------------------------
# Game state
# ----------------------------
scroll_x = 0
player_x = WIDTH // 2
player_speed = 5

# ----------------------------
# Main loop
# ----------------------------
running = True
while running:
    dx = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ----------------------------
        # Keyboard SFX
        # ----------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                right_sfx.play()
            elif event.key == pygame.K_s:
                wrong_sfx.play()

        # ----------------------------
        # Controller SFX
        # ----------------------------
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # A button
                right_sfx.play()
            elif event.button == 1:  # B button
                wrong_sfx.play()

    # ----------------------------
    # Movement input
    # ----------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        dx = player_speed
    if keys[pygame.K_LEFT]:
        dx = -player_speed

    # Controller analog stick
    if joystick:
        axis = joystick.get_axis(0)
        if abs(axis) > 0.2:  # deadzone
            dx = int(axis * player_speed)

    # ----------------------------
    # Update scrolling
    # ----------------------------
    player_x += dx

    if player_x > WIDTH // 2:
        scroll_x += dx
        player_x = WIDTH // 2

    if player_x < WIDTH // 4:
        scroll_x += dx
        player_x = WIDTH // 4

    # ----------------------------
    # Drawing
    # ----------------------------
    screen.fill((135, 206, 235))  # sky blue

    # 🌄 Far background (slow)
    for i in range(5):
        pygame.draw.rect(
            screen,
            (100, 100, 255),
            (i * 300 - scroll_x * 0.2, 80, 200, 120),
        )

    # 🌳 Mid layer
    for i in range(10):
        pygame.draw.rect(
            screen,
            (50, 200, 50),
            (i * 200 - scroll_x * 0.5, 200, 100, 100),
        )

    # 🌱 Foreground
    for i in range(20):
        pygame.draw.rect(
            screen,
            (20, 150, 20),
            (i * 100 - scroll_x, 300, 50, 50),
        )

    # 🧍 Player
    pygame.draw.rect(screen, (200, 50, 50), (player_x, 250, 40, 40))

    # ----------------------------
    # Display
    # ----------------------------
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()