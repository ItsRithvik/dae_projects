import tensorflow as tf
import gymnasium as gym
import keras as rl
import ale_py
import random

#creating enviroment
gym.register_envs(ale_py)
env = gym.make('ALE/Breakout-v5',render_mode='human')

#assigning number of possible states/actions
states = env.observation_space.shape[0]
actions = env.action_space.n

episodes = 5
for episode in range(1,episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0,1,2,3])
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode {}: {}'.format(episode, score))
env.close()


# for episode in range(1, 6):
#     state = env.reset()
#     done = False
#     score = 0
#     while not done:
#         env.render(none)
#         action = random.choice([0,1,2,3])
#         n_state, reward, done, info = gym.env.step(action)
#         score += reward
#         print('Episode {}: {}'.format(episode, score))