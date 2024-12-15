import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

class AdvancedClimateEnv(gym.Env):
    def __init__(self):
        super(AdvancedClimateEnv, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(5,))
        self.action_space = gym.spaces.Discrete(4)
        self.state = np.random.uniform(0.4, 0.6, size=(5,))

    def step(self, action):
        reward = 0
        if action == 0:  # Carbon capture
            self.state[0] -= np.random.uniform(0.01, 0.05)
        elif action == 1:  # Renewable energy
            self.state[1] -= np.random.uniform(0.02, 0.06)
        elif action == 2:  # Afforestation
            self.state[2] -= np.random.uniform(0.03, 0.07)
        elif action == 3:  # Geoengineering
            self.state[3] -= np.random.uniform(0.04, 0.08)

        reward = -np.sum(np.maximum(0, self.state - 0.2))
        done = np.all(self.state <= 0.2)
        return self.state, reward, done, {}

    def reset(self):
        self.state = np.random.uniform(0.4, 0.6, size=(5,))
        return self.state

if __name__ == "__main__":
    env = AdvancedClimateEnv()
    check_env(env)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=50000)
    model.save("models/advanced_intervention_optimizer")
    print("Advanced intervention optimizer saved.")
