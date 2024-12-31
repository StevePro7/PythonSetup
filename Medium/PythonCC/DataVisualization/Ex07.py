# 07. Physics Simulation
import numpy as np

# Initialize positions (x, y) and velocities (vx, vy) for 5 objects
positions = np.random.rand(5, 2) * 100  # Initial positions
velocities = np.zeros((5, 2))           # Initial velocities
gravity = np.array([0, -9.8])           # Gravity (m/s²)
time_step = 0.1                         # Time step (s)

# Simulate for 10 seconds
for _ in range(int(10 / time_step)):
    velocities += gravity * time_step
    positions += velocities * time_step

# Print final positions
print("Final Positions of Objects:")
print(positions)