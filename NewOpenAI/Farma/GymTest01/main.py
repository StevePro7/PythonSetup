import gym

name = "FrozenLake-v1"
env = gym.make(name, render_mode="human")
env.reset()
env.render()

env.observation_space
env.action_space

retVal = env.step(1)
result = env.P[0][1]
env.close()