# Smart Energy Lader - Architecture Documentation

## Project Overview

Smart Energy Lader is an AI-powered energy optimization system for Factory I/O industrial automation environments. It uses Reinforcement Learning (RL) to optimize energy consumption while maintaining throughput and system efficiency.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Factory I/O Simulation                    │
│  (14 Conveyors, 4 Pushers, 3 Pick-Place Robots, Sensors)   │
└────────────────┬────────────────────────────────────────────┘
                 │ Modbus Communication
                 ↓
┌─────────────────────────────────────────────────────────────┐
│              RL Training Environment (Gym)                   │
│                  FactoryEnergyEnv                            │
│  - Observation Space: (10,) - Factory state variables        │
│  - Action Space: Discrete(8) - Machine sequencing            │
│  - Reward: Energy minimization + Load balancing              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────┐
│              PPO Agent (Stable-Baselines3)                   │
│  - Policy Network: MLP [256, 256, 128] units                 │
│  - Training: 100,000+ timesteps                              │
│  - Hyperparameters: α=3e-4, γ=0.99, λ=0.95                  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────┐
│          Streamlit Dashboard (Real-time Monitoring)          │
│  - Live power consumption tracking                           │
│  - AI decision explanations                                  │
│  - Manual override capabilities                              │
│  - Performance analytics                                     │
└─────────────────────────────────────────────────────────────┘
```

## Component Descriptions

### 1. Data Simulation (notebooks/01_data_simulation.ipynb)
- Generates synthetic Factory I/O operational data
- Models realistic machine behavior profiles
- Outputs time-series power consumption data
- Supports batch scenario generation

**Key Functions:**
- `simulate_conveyor_operation()` - 14 conveyor units
- `simulate_pusher_operation()` - 4 actuator units
- `simulate_robot_operation()` - 3 pick-place robots

### 2. RL Training Pipeline (notebooks/02_rl_training.ipynb)
- Implements `FactoryEnergyEnv` Gym-compatible environment
- Trains PPO agent for energy optimization
- Saves checkpoints during training
- Validates model performance

**Environment Details:**
```python
class FactoryEnergyEnv(gym.Env):
    - Observation: [conveyor_power, pusher_power, robot_power, 
                    total_power, loads_x3, timestamp, energy, reward]
    - Action: 8 discrete choices for machine sequencing
    - Reward: -total_power/40 - 0.1*load_imbalance
```

### 3. Model Validation (notebooks/03_model_validation.ipynb)
- Loads trained RL model
- Evaluates policy performance
- Generates performance metrics
- Creates comparison visualizations

**Metrics Calculated:**
- Mean/std reward per episode
- Total energy consumption
- Average power draw
- Episode lengths

### 4. Performance Analysis (notebooks/04_performance_analysis.ipynb)
- Compares baseline vs optimized performance
- Statistical significance testing
- Performance visualizations
- Exports results for reporting

**Analysis Includes:**
- t-tests for statistical significance
- Cohen's d effect sizes
- Power distribution analysis
- Energy savings calculations

### 5. Dashboard (dashboard/app.py)
- Real-time monitoring interface
- Interactive factory layout visualization
- AI control panel with manual overrides
- Performance metrics and KPIs

**Features:**
- Live power consumption graphs
- System efficiency tracking
- Component status indicators
- Data export functionality

## Model Training Details

### PPO Hyperparameters
```
learning_rate: 3e-4
batch_size: 64
n_steps: 2048
n_epochs: 10
gamma: 0.99
gae_lambda: 0.95
```

### Training Process
1. Initialize environment with factory specifications
2. Train model for 100,000 timesteps
3. Save checkpoints every 10,000 steps
4. Monitor reward curves with TensorBoard
5. Evaluate on validation scenarios

### Expected Performance
- **Energy Reduction**: 18-25% vs baseline
- **Peak Power Reduction**: 45% vs unoptimized spikes
- **Machine Utilization**: ≥95% maintained
- **Training Time**: 30-60 minutes on standard GPU

## Data Flow

### Input Data
- Factory state: Power, loads, operational parameters
- Modbus registers: Sensor readings, device status
- System constraints: Power limits, safety margins

### Processing
1. Read current state from Factory I/O via Modbus
2. Extract observations (10-dimensional state vector)
3. Pass to RL agent for action selection
4. Execute action (adjust machine scheduling)
5. Measure reward (energy consumed, system performance)

### Output Data
- AI decision: Selected action with confidence score
- Power optimization: Expected kW savings
- Predicted outcomes: Estimated efficiency, throughput
- Audit logs: Decision history for analysis

## Integration Points

### Factory I/O
- Modbus TCP communication
- Register mapping for observations/actions
- Scene files for component configuration

### LabVIEW (Optional)
- JSON/CSV data export for LabVIEW integration
- Socket-based communication stubs
- Data serialization helpers

### External Monitoring
- CSV/JSON report generation
- Real-time dashboard via Streamlit
- Performance metrics export

## Performance Optimization Strategies

1. **Load Balancing**: Distribute work evenly across machines
2. **Startup Surge Reduction**: Stagger machine activation
3. **Idle Power Minimization**: Reduce holding currents
4. **Peak Shaving**: Smooth power consumption curves

## Safety Considerations

- Minimum throughput maintained at 95%
- Hard power limits enforced
- Manual override capability at all times
- Graceful degradation on model uncertainty
- Emergency stop functionality

## File Structure

```
smart-energy-lader/
├── notebooks/
│   ├── 01_data_simulation.ipynb
│   ├── 02_rl_training.ipynb
│   ├── 03_model_validation.ipynb
│   └── 04_performance_analysis.ipynb
├── dashboard/
│   ├── app.py
│   ├── components/
│   │   ├── layout.py
│   │   └── metrics.py
│   └── requirements.txt
├── models/
│   ├── trained_rl_model.pkl
│   └── model_architecture.py
├── factory_io/
│   ├── factory_io_utils.py
│   ├── scene_files/
│   └── modbus_config/
├── labview/
│   ├── labview_integration.py
│   └── ai_integration_examples/
├── docs/
│   ├── architecture.md
│   └── setup_guide.md
├── tests/
├── .github/workflows/
│   └── test.yml
├── requirements.txt
├── README.md
└── demo_script.py
```

## Technologies Used

- **Python 3.9+**
- **Stable-Baselines3** (RL library)
- **Gym** (RL environment)
- **Streamlit** (Dashboard)
- **Plotly** (Visualizations)
- **Pandas/NumPy** (Data processing)
- **PyTest** (Testing)
- **GitHub Actions** (CI/CD)

## Future Enhancements

1. Multi-agent RL for distributed control
2. Real-time model retraining with new data
3. Advanced visualization with 3D factory layout
4. Integration with more sensors (temperature, vibration)
5. Predictive maintenance based on power patterns
6. Cost optimization considering time-of-use electricity rates
