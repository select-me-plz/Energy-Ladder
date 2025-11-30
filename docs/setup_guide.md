# Smart Energy Lader - Setup Guide

## Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment tool (venv or conda)
- 4GB+ RAM recommended
- GPU optional (for faster training)

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/your-username/smart-energy-lader.git
cd smart-energy-lader
```

### 2. Create Virtual Environment

#### Using Python venv:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### Using Conda:
```bash
conda create -n smart-energy-lader python=3.9
conda activate smart-energy-lader
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install -r dashboard/requirements.txt
```

### 4. Verify Installation
```bash
python -c "import gym; import stable_baselines3; import streamlit; print('All dependencies installed!')"
```

## Running the Notebooks

### 1. Start Jupyter
```bash
jupyter notebook
```

### 2. Run Notebooks in Order

Navigate to the `notebooks/` directory and open:

1. **01_data_simulation.ipynb** - Generate synthetic data
2. **02_rl_training.ipynb** - Train the RL model
3. **03_model_validation.ipynb** - Validate trained model
4. **04_performance_analysis.ipynb** - Analyze performance

## Running the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open at `http://localhost:8501`

### Dashboard Features
- Real-time power consumption monitoring
- Interactive factory layout visualization
- AI control panel with manual overrides
- Performance metrics and statistics
- Data export functionality

## Running the Demo Script

```bash
python demo_script.py
```

This demonstrates:
1. Loading the trained model
2. Running baseline simulation
3. Running optimized simulation
4. Displaying comparison results

## Testing

### Run Unit Tests
```bash
pytest tests/ -v
```

### Run Linting
```bash
flake8 . --max-line-length=120
```

### Run Type Checking
```bash
mypy . --ignore-missing-imports
```

## Configuration

### Modifying Factory Specifications
Edit `factory_specs` in notebooks or demo_script.py:
```python
factory_specs = {
    'conveyors': {'count': 14, 'max_power': 28},
    'pushers': {'count': 4, 'max_power': 12},
    'pick_place': {'count': 3, 'max_power': 12}
}
```

### Adjusting RL Hyperparameters
Modify in `02_rl_training.ipynb`:
```python
model = PPO(
    "MlpPolicy",
    vec_env,
    learning_rate=3e-4,  # Adjust learning rate
    batch_size=64,       # Adjust batch size
    n_steps=2048,        # Adjust step count
    gamma=0.99           # Adjust discount factor
)
```

### Dashboard Customization
Edit `dashboard/app.py`:
- Change title and styling
- Modify metric calculations
- Add new visualizations
- Customize sidebar controls

## Factory I/O Integration

### Modbus Setup
1. Configure Factory I/O scene with Modbus server
2. Create register mapping in `factory_io/modbus_config/`
3. Update `FactoryEnergyEnv` with register addresses
4. Run environment with live Factory I/O connection

### LabVIEW Integration
1. Use `labview/labview_integration.py` helpers
2. Export AI decisions via JSON: `export_for_labview()`
3. Import system data via: `import_from_labview()`
4. Implement socket/file-based handshake

## Troubleshooting

### Issue: Missing dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Jupyter notebook not starting
```bash
pip install --upgrade jupyter ipykernel
python -m ipykernel install --user
```

### Issue: Streamlit port already in use
```bash
streamlit run dashboard/app.py --server.port 8502
```

### Issue: Model training very slow
- Check GPU availability: `nvidia-smi`
- Install GPU support: `pip install torch-cuda` (if not installed)
- Reduce `n_steps` or `batch_size`

### Issue: Environment step fails
- Verify `FactoryEnergyEnv` initialization parameters
- Check state space boundaries (0-100)
- Ensure action space is discrete 0-7

## Performance Tips

1. **Training Speed**: Use GPU when available
   ```bash
   pip install torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Dashboard Performance**: Limit data refresh rate
   - Edit `dashboard/app.py` update frequency
   - Use session caching for static data

3. **Memory Usage**: Use vectorized environments
   ```python
   from stable_baselines3.common.vec_env import DummyVecEnv
   vec_env = DummyVecEnv([lambda: env])
   ```

## Next Steps

1. **Collect Real Data**: Replace simulated data with actual Factory I/O logs
2. **Fine-tune Model**: Retrain on your specific factory configuration
3. **Deploy Dashboard**: Host Streamlit on cloud platform
4. **Monitor Production**: Set up continuous monitoring in live environment
5. **Advanced Integration**: Connect with existing MES/SCADA systems

## Support & Documentation

- **API Documentation**: See docstrings in Python files
- **Architecture Details**: See `docs/architecture.md`
- **Examples**: Explore Jupyter notebooks
- **Community**: Contribute via GitHub issues/PRs

## License

This project is licensed under the MIT License - see LICENSE file for details

## References

- Stable-Baselines3: https://stable-baselines3.readthedocs.io/
- OpenAI Gym: https://gym.openai.com/
- Streamlit: https://streamlit.io/
- Factory I/O: https://factoryio.com/
