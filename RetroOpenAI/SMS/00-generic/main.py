import retro

name = "TransBot-Sms"

try:
    env = retro.make(game=name, record='.')
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
