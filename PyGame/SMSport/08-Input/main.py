import pygame
from func import apply_deadzone

pygame.init()
pygame.joystick.init()

pygame.display.set_caption("Input example")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

joystick_count = pygame.joystick.get_count()
print(f"Connected controllers: {joystick_count}")

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Controller name:", joystick.get_name())

DEADZONE = 0.15
INV_RANGE = 1.0 / (1.0 - DEADZONE)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYBUTTONDOWN:
            print("Button pressed:", event.button)

        lx_raw = joystick.get_axis(0)
        ly_raw = joystick.get_axis(1)
        rx_raw = joystick.get_axis(3)
        ry_raw = joystick.get_axis(4)

        lx = apply_deadzone(lx_raw, DEADZONE, INV_RANGE)
        ly = apply_deadzone(ly_raw, DEADZONE, INV_RANGE)
        rx = apply_deadzone(rx_raw, DEADZONE, INV_RANGE)
        ry = apply_deadzone(ry_raw, DEADZONE, INV_RANGE)

        lx *= abs(lx)
        ly *= abs(ly)
        rx *= abs(rx)
        ry *= abs(ry)

#        print(lx)

        if event.type == pygame.JOYHATMOTION:
            print("D-pad:", event.value)

    # Read all axes
    lt_raw = joystick.get_axis(4)
    rt_raw = joystick.get_axis(5)

    # Normalize
    lt = (lt_raw + 1) / 2
    rt = (rt_raw + 1) / 2

    #print(f"LT: {lt:.2f}  RT: {rt:.2f}")

    if lt > 0.2:
        print(f"Left trigger active {lt}")

    if rt > 0.2:
        print(f"Right trigger active {rt}")

    # --- Alternative: combined axis (Linux/macOS) ---
    # elif len(axes) >= 3:
    #     trigger = axes[2]
    #
    #     if trigger < 0:
    #         print(f"LT: {-trigger:.2f}")
    #     elif trigger > 0:
    #         print(f"RT: {trigger:.2f}")

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()