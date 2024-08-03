import gymnasium as gym

name = "FrozenLake-v1"

try:
    env = gym.make(name, render_mode="human")
    env.reset()
    env.render()

    # observation space - states
    env.observation_space

    # actions: left -0, down - 1, right - 2, up- 3
    env.action_space

    randomAction= env.action_space.sample()
    returnValue = env.step(randomAction)
    # format of returnValue is (observation,reward, terminated, truncated, info)
    # observation (object)  - observed state
    # reward (float)        - reward that is the result of taking the action
    # terminated (bool)     - is it a terminal state
    # truncated (bool)      - it is not important in our case
    # info (dictionary)     - in our case transition probability

    env.render()

    # perform deterministic step 0,1,2,3
    returnValue = env.step(1)
    env.reset()

    # env.P[state][action]
    temp: list = env.P[0][1]
    # output is a list having the following entries
    # (transition probability, next state, reward, Is terminal state?)

    env.close()
except KeyboardInterrupt:
    exit(0)