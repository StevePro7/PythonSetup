import gymnasium as gym

name = 'Acrobot-v1'
#name = 'CartPole-v1'
#name = 'MountainCarContinuous-v0'
#name = 'MountainCar-v0'
#name = "Pendulum-v1"

try:
    env = gym.make(name, render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        _, reward, terminated, truncated, _ = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()
except KeyboardInterrupt:
    exit(0)
