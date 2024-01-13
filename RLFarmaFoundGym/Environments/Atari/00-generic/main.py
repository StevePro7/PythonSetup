import gymnasium as gym


name = "ALE/Zaxxon-v5"

try:
    env = gym.make(name, render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()
except KeyboardInterrupt:
    exit(0)
    