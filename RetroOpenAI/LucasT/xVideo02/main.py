import argparse
import retro


env = retro.make(game='SonicTheHedgehog2-Genesis', state='AquaticRuinZone.Act2')
env.reset()

done = False
try:
    while not done:
        env.render()
        #action = env.action_space.sample()
        action = [0,0,1,0,0,0,0,1,1,1,0,0]
        #print(action)
        ob, rew, done, info = env.step(action)

    print('the end')

except KeyboardInterrupt:
    exit(0)
