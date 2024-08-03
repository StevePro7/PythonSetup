import gym
import time

env=gym.make("FrozenLake-v1",render_mode='human')
env.reset()
env.render()
print('Initial state of the system')

numberOfIterations=30

for i in range(numberOfIterations):
    randomAction= env.action_space.sample()
    returnValue = env.step(randomAction)
    env.render()
    print(f"Iteration: {i+1} and action {randomAction}")
    time.sleep(2)
    if returnValue[2]:
        break

env.close()
