import gymnasium as gym

def run_game(name: str) -> None:
    """
    This is the file
    :param name: Name of the video game
    :return: None
    """
    try:
        env = gym.make(name, render_mode="human")
        observation, info = env.reset()

        for _ in range(1000):
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                observation, info = env.reset()

        env.close()
    except KeyboardInterrupt:
        exit(0)