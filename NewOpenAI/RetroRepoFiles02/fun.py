import retro


def run_game(name: str) -> None:
    try:
        env = retro.make(game=name)
        observation, info = env.reset()

        while True:
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                observation, info = env.reset()

        env.close()
    except KeyboardInterrupt:
        exit(0)