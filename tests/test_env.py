"""
Unit tests for RL environment.
"""

import pytest
import numpy as np
import gym
from gym import spaces


class TestFactoryEnergyEnv:
    """Test suite for FactoryEnergyEnv."""
    
    @pytest.fixture
    def env(self):
        """Create test environment."""
        factory_specs = {
            'conveyors': {'count': 14, 'max_power': 28},
            'pushers': {'count': 4, 'max_power': 12},
            'pick_place': {'count': 3, 'max_power': 12}
        }
        
        # Import here to avoid issues
        from notebooks.code_training import FactoryEnergyEnv
        return FactoryEnergyEnv(factory_specs, max_steps=100)
    
    def test_environment_initialization(self, env):
        """Test environment initializes correctly."""
        assert isinstance(env.action_space, gym.Space)
        assert isinstance(env.observation_space, gym.Space)
        assert env.action_space.n == 8
        assert env.observation_space.shape == (10,)
    
    def test_reset_returns_valid_state(self, env):
        """Test reset returns valid initial state."""
        state = env.reset()
        
        assert isinstance(state, np.ndarray)
        assert state.shape == (10,)
        assert np.all(state >= 0)
        assert np.all(state <= 100)
    
    def test_step_returns_valid_output(self, env):
        """Test step returns valid output."""
        env.reset()
        action = env.action_space.sample()
        
        next_state, reward, done, info = env.step(action)
        
        assert isinstance(next_state, np.ndarray)
        assert isinstance(reward, (float, np.floating))
        assert isinstance(done, (bool, np.bool_))
        assert isinstance(info, dict)
    
    def test_episode_termination(self, env):
        """Test episode terminates correctly."""
        env.reset()
        done = False
        steps = 0
        
        while not done and steps < 200:
            action = env.action_space.sample()
            _, _, done, _ = env.step(action)
            steps += 1
        
        assert done
        assert steps <= 100


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
