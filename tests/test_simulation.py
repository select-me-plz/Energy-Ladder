"""
Unit tests for data simulation module.
"""

import pytest
import numpy as np
from notebooks.code_simulation import (
    simulate_conveyor_operation,
    simulate_pusher_operation,
    simulate_robot_operation,
    generate_operational_scenarios
)


class TestDataSimulation:
    """Test suite for data simulation functions."""
    
    def test_conveyor_simulation_output_shape(self):
        """Test conveyor simulation returns correct shape."""
        duration = 100
        num_conveyors = 14
        timesteps, power = simulate_conveyor_operation(duration, num_conveyors)
        
        assert len(timesteps) == len(power)
        assert power.min() > 0
        assert power.max() <= num_conveyors * 5
    
    def test_pusher_simulation_output_shape(self):
        """Test pusher simulation returns correct shape."""
        duration = 100
        num_pushers = 4
        timesteps, power = simulate_pusher_operation(duration, num_pushers)
        
        assert len(timesteps) == len(power)
        assert power.min() >= 0
        assert power.max() <= num_pushers * 5
    
    def test_robot_simulation_output_shape(self):
        """Test robot simulation returns correct shape."""
        duration = 100
        num_robots = 3
        timesteps, power = simulate_robot_operation(duration, num_robots)
        
        assert len(timesteps) == len(power)
        assert power.min() >= 0
        assert power.max() <= num_robots * 5
    
    def test_operational_scenarios_generation(self):
        """Test operational scenario generation."""
        machine_profiles = {
            'conveyors': {'count': 14, 'startup_surge': 2.0, 'run_power': 1.0},
            'pushers': {'count': 4, 'activation_surge': 3.0, 'hold_power': 0.5},
            'pick_place': {'count': 3, 'peak_power': 4.0, 'idle_power': 0.2}
        }
        
        df = generate_operational_scenarios(machine_profiles, duration_seconds=360)
        
        assert 'timestamp' in df.columns
        assert 'total_power' in df.columns
        assert len(df) > 0
        assert df['total_power'].min() > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
