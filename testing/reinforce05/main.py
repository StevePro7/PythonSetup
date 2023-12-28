import retro

def print_hi(name):
    print(f'Hi, {name}')
    env = retro.make(game='Strider-Genesis', record='.')
    env.reset()
    done = False
    while not done:
        env.render()
        obs, rew, done, info = env.step(env.action_space.sample())
        if done:
            env.reset()

    env.close()

if __name__ == '__main__':
    print_hi('PyCharm.X.')

