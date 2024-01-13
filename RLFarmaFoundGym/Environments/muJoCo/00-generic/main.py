import gymnasium as gym

name ="Ant-v4"
#name ="HalfCheetah-v4"
#name ="Hopper-v4"
#name ="Humanoid-v4"
#name ="HumanoidStandup-v4"
#name ="InvertedDoublePendulum-v4"
#name ="InvertedPendulum-v4"
#name ="Pusher-v4"
#name ="Reacher-v4"
#name ="Swimmer-v4"
#name ="Walker2d-v4"

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
