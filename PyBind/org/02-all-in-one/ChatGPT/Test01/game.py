import game
import time

# Simulate game control with Python
commands = ['w', 'a', 's', 'd', 'd', 's', 'a']

print("Starting game...")
for command in commands:
    print(f"Sending command: {command}")
    game.step_game(command)
    time.sleep(0.5)
