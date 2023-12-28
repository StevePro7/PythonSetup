import retro

def print_hi(name):
    print(f'Hi, {name}')
    env = retro.make(game='Airstriker-Genesis', record='.')
    3#env = retro.make(game='Strider-Genesis', record='.')
    env = retro.make(game='Strider-Genesis')
    print(env)


if __name__ == '__main__':
    print_hi('PyCharm!!')
