import gymnasium as gym

# https://www.gymlibrary.dev/index.html
# https://www.gymlibrary.dev/environments/atari/up_n_down
#name = "ALE/Zaxxon-v5"
#name = "ALE/UpNDown-v5"
name = "ALE/Breakout-v5"
#name = "Acrobot-v1"
#name = "Taxi-v3"
#name = "BipedalWalker-v3"
#name = "Ant-v4"
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