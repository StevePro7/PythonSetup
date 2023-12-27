import argparse
#import retro

parser = argparse.ArgumentParser()
parser.add_argument('--game', default='SuperMarioBros-Nes', help='the name or path for the game to run')
parser.add_argument('--state', help='the initial state file to load, minus the extension')
args = parser.parse_args()

def main():
    print(args.game)
    print(args.state)

    env = retro.make(ags.game, args.state or retro.State.DEFAULT, record=args.record)
    obs = env.reset()

    total_reward = 0

    while True:
        # env.step returns 4 parameters
        # observ    object representing your observation of the environment
        # reward    a floating point number of the reward from the previous action
        # done      boolean value indicating whether or not to reset the environment
        # info      a dictionary containing data from the game vars defined in data.json
        # action    env.action_space.sample()   do a random action
        # action    [0,0,1,0,0,0,0,1,1,1,0,0]   input vector
        # print(env.action_space.sample())
        observ, reward, done, info = env.step(env.action_space.simple())

        # add up the total rewards gained
        total_reward += reward
        # mario - unsigned single byte (8bit); xscrollLo wraps at 255 and increases xscrollHi by 1
        print("Reward: ", reward, "Total Reward: ", total_reward, "score:", info['score'], "levelLo:", info['levelLo'],
              "xscrollHi:", info['xscrollHi'], "xscrollLo:", info['xscrollLo'], "scrolling:", info['scrolling'])
        # sonic2 - unsigned double byte (16bit); makes it a lot easier to work with
        # print("Reward: ", reward, "Total Reward: ", total_reward, "screen_x_end:", info['screen_x_end'], "x:", info['x'], "y:", info['y'])

        # render the game. not displaying hte screen will speed things up
        env.render()

        if done:
            obs = env.reset()

    env.close()

if __name__ == '__main__':
    main()
