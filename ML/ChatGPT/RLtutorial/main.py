# Step 1: Install Required Libraries
# Step 2: Define the Environment
import numpy as np
import random
import matplotlib.pyplot as plt

# Define grid world dimensions
grid_size = 5
goal_state = (0, 4)  # Goal is at the top-right corner
start_state = (4, 0)  # Start at the bottom-left corner

# Define actions: Up, Down, Left, Right
actions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # (dx, dy)

# Q-table: initialize with zeros (5x5 grid, each cell has 4 possible actions)
Q = np.zeros((grid_size, grid_size, len(actions)))

# Reward setup: -1 for each step, +10 for reaching the goal
rewards = np.full((grid_size, grid_size), -1)
rewards[goal_state] = 10

# Parameters for Q-learning
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1  # Exploration rate


# Step 3: Define the Agent’s Movement and Q-Update
def choose_action(state):
    """Choose action using epsilon-greedy strategy"""
    if random.uniform(0, 1) < epsilon:
        return random.choice(range(len(actions)))  # Explore
    else:
        return np.argmax(Q[state[0], state[1]])  # Exploit the best known action

def update_Q(state, action, reward, next_state):
    """Update Q-table using the Q-learning formula"""
    best_next_action = np.argmax(Q[next_state[0], next_state[1]])
    Q[state[0], state[1], action] += learning_rate * (reward + discount_factor * Q[next_state[0], next_state[1], best_next_action] - Q[state[0], state[1], action])


# Step 4: Simulate the Learning Process
def run_episode():
    state = start_state
    total_reward = 0

    while state != goal_state:
        action = choose_action(state)
        next_state = (state[0] + actions[action][0], state[1] + actions[action][1])

        # Ensure the agent stays within grid boundaries
        next_state = (max(0, min(grid_size - 1, next_state[0])), max(0, min(grid_size - 1, next_state[1])))

        reward = rewards[next_state]
        total_reward += reward

        # Update Q-table
        update_Q(state, action, reward, next_state)

        # Move to next state
        state = next_state

    return total_reward


# Run multiple episodes to learn
episodes = 1000
for episode in range(episodes):
    run_episode()

print("Training completed.")


# Step 5: Visualize the Learned Policy
# Visualize the learned policy
policy_grid = np.full((grid_size, grid_size), '')
for i in range(grid_size):
    for j in range(grid_size):
        best_action = np.argmax(Q[i, j])
        if best_action == 0:
            policy_grid[i, j] = '↑'
        elif best_action == 1:
            policy_grid[i, j] = '↓'
        elif best_action == 2:
            policy_grid[i, j] = '←'
        else:
            policy_grid[i, j] = '→'

# Plot the grid
plt.imshow(np.ones((grid_size, grid_size)), cmap='Blues')
for i in range(grid_size):
    for j in range(grid_size):
        plt.text(j, i, policy_grid[i, j], ha='center', va='center', fontsize=12, color='black')

plt.title("Learned Policy")
plt.show()