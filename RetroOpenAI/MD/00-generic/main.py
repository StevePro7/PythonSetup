import retro

name = "Strider-Genesis"

try:
    env = retro.make(game='Strider-Genesis', record='.')
    env.reset()
    done = False
    while not done:
        env.render()
        obs, rew, done, info = env.step(env.action_space.sample())
        if done:
            env.reset()

    env.close()
except KeyboardInterrupt:
    exit(0)
