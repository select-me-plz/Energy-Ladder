"""
Configuration file for Smart Energy Lader
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"

# Create directories if they don't exist
for directory in [DATA_DIR, MODELS_DIR]:
    directory.mkdir(exist_ok=True)

# Factory specifications
FACTORY_SPECS = {
    'conveyors': {
        'count': 14,
        'max_power': 28,  # kW
        'startup_surge': 2.0,
        'run_power': 1.0,
        'efficiency': 0.92
    },
    'pushers': {
        'count': 4,
        'max_power': 12,  # kW
        'activation_surge': 3.0,
        'hold_power': 0.5,
        'efficiency': 0.88
    },
    'pick_place': {
        'count': 3,
        'max_power': 12,  # kW
        'peak_power': 4.0,
        'idle_power': 0.2,
        'efficiency': 0.90
    }
}

# RL Training Configuration
RL_CONFIG = {
    'learning_rate': 3e-4,
    'batch_size': 64,
    'n_steps': 2048,
    'n_epochs': 10,
    'gamma': 0.99,
    'gae_lambda': 0.95,
    'total_timesteps': 100000
}

# Environment Configuration
ENV_CONFIG = {
    'max_steps': 3600,
    'observation_dim': 10,
    'action_dim': 8,
    'reward_scaling': 1.0
}

# Modbus Configuration
MODBUS_CONFIG = {
    'host': 'localhost',
    'port': 502,
    'slave_id': 1,
    'polling_interval': 0.1  # seconds
}

# Dashboard Configuration
DASHBOARD_CONFIG = {
    'page_title': 'Smart Energy Lader - Factory I/O Dashboard',
    'page_icon': '⚡',
    'layout': 'wide',
    'theme': 'light'
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'log_file': PROJECT_ROOT / 'logs' / 'smart_energy_lader.log'
}
