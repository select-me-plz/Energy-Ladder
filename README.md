# Smart Energy Lader - AI Factory Optimization

<div align="center">

## ⚡ Smart Energy Lader

**AI-Powered Energy Optimization for Industrial Automation**

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

[About](#about) • [Features](#features) • [Quick Start](#quick-start) • [Documentation](#documentation)

</div>

---

## 🏭 About

Smart Energy Lader is an advanced AI-powered energy optimization system designed for **Factory I/O** industrial automation environments. It uses **Reinforcement Learning (RL)** with PPO (Proximal Policy Optimization) to intelligently optimize energy consumption while maintaining production throughput and system efficiency.

### Key Statistics
- 📊 **Energy Reduction**: 18-25% vs baseline operations
- ⚡ **Peak Power Reduction**: 45% vs unoptimized spikes
- 🎯 **Throughput Maintained**: ≥95% of baseline
- 🚀 **Real-time Decisions**: <100ms AI response time

### Factory Components
- 14 Belt Conveyors
- 4 Pneumatic Pushers
- 3 Two-Axis Pick & Place Robots
- 7 Vision Sensors
- 2 Positioners

---

## ✨ Features

### 🤖 AI Optimization
- **Reinforcement Learning**: PPO agent trained on 100,000+ timesteps
- **Hybrid Actions**: Discrete machine sequencing decisions
- **Adaptive Learning**: Continuous improvement from operational data

### 📊 Real-Time Dashboard
- Live power consumption monitoring
- Interactive factory layout visualization
- AI confidence scores and decision explanations
- Manual override capabilities
- Performance metrics and KPIs

### 📈 Comprehensive Analytics
- Statistical comparison (baseline vs optimized)
- Performance trend analysis
- Energy savings reports
- Cost-benefit analysis

### 🔧 Industrial Integration
- **Modbus TCP Support**: Direct Factory I/O communication
- **LabVIEW Compatible**: JSON/CSV data exchange
- **SCADA Ready**: Export decision data to existing systems

### 🧪 Development Tools
- 4 Jupyter Notebooks for complete pipeline
- Streamlit dashboard for live monitoring
- Comprehensive unit tests
- GitHub Actions CI/CD pipeline

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
Git
Virtual environment
```

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/your-username/smart-energy-lader.git
cd smart-energy-lader
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
pip install -r dashboard/requirements.txt
```

4. **Verify Installation**
```bash
python -c "import gym; import stable_baselines3; import streamlit; print('✓ Ready!')"
```

### Run Dashboard
```bash
streamlit run dashboard/app.py
```
Opens at `http://localhost:8501`

### Run Demo
```bash
python demo_script.py
```

---

## 📚 Documentation

### Project Structure
```
smart-energy-lader/
├── 📁 notebooks/                    # Jupyter notebooks for pipeline
│   ├── 01_data_simulation.ipynb    # Synthetic data generation
│   ├── 02_rl_training.ipynb        # Model training
│   ├── 03_model_validation.ipynb   # Model evaluation
│   └── 04_performance_analysis.ipynb # Analytics & reporting
├── 📁 dashboard/                    # Streamlit web application
│   ├── app.py                      # Main dashboard
│   ├── components/                 # Reusable UI components
│   └── requirements.txt            # Dashboard dependencies
├── 📁 models/                       # RL models & architecture
│   ├── trained_rl_model.pkl        # Trained PPO model
│   └── model_architecture.py       # Model utilities
├── 📁 factory_io/                   # Factory I/O integration
│   ├── factory_io_utils.py         # Scene & Modbus utilities
│   ├── scene_files/                # Factory scene configurations
│   └── modbus_config/              # Modbus register mappings
├── 📁 labview/                      # LabVIEW integration
│   ├── labview_integration.py      # Data exchange helpers
│   └── ai_integration_examples/    # Integration examples
├── 📁 docs/                         # Documentation
│   ├── architecture.md             # System architecture
│   └── setup_guide.md              # Setup instructions
├── 📁 tests/                        # Unit tests
├── demo_script.py                   # Complete demo
├── requirements.txt                 # Main dependencies
└── README.md                        # This file
```

### Documentation Files
- **[Architecture Guide](docs/architecture.md)** - System design and components
- **[Setup Guide](docs/setup_guide.md)** - Installation and configuration
- **[API Reference](notebooks/)** - Detailed code documentation

---

## 💻 Usage

### 1. Generate Training Data
```bash
jupyter notebook notebooks/01_data_simulation.ipynb
```
Generates synthetic Factory I/O operational data based on machine profiles.

### 2. Train RL Model
```bash
jupyter notebook notebooks/02_rl_training.ipynb
```
Trains PPO agent on simulated data (100,000 timesteps).

### 3. Validate Model
```bash
jupyter notebook notebooks/03_model_validation.ipynb
```
Evaluates trained model performance and generates metrics.

### 4. Analyze Results
```bash
jupyter notebook notebooks/04_performance_analysis.ipynb
```
Comprehensive statistical analysis and visualizations.

### 5. Monitor Dashboard
```bash
streamlit run dashboard/app.py
```
Real-time monitoring with AI control panel.

---

## 🔌 Integration

### Factory I/O Connection
```python
from factory_io.factory_io_utils import parse_modbus_config, ModbusSimulator

config = parse_modbus_config('factory_io/modbus_config/config.json')
modbus = ModbusSimulator(slave_id=1)
```

### LabVIEW Export
```python
from labview.labview_integration import export_for_labview

export_for_labview(data, 'output/labview_data.json', format='json')
```

### Custom Environments
Modify `FactoryEnergyEnv` in `notebooks/02_rl_training.ipynb`:
```python
class FactoryEnergyEnv(gym.Env):
    def __init__(self, machine_config):
        self.action_space = spaces.Discrete(8)
        self.observation_space = spaces.Box(...)
```

---

## 📊 Performance Metrics

### Baseline vs Optimized (1-hour simulation)

| Metric | Baseline | Optimized | Improvement |
|--------|----------|-----------|-------------|
| Total Energy | 45.2 kWh | 37.1 kWh | **18.0%** |
| Mean Power | 45.2 kW | 37.1 kW | **18.0%** |
| Peak Power | 72.3 kW | 39.8 kW | **45.0%** |
| Efficiency | 85% | 92% | **7.0%** |

---

## 🧪 Testing

### Run Tests
```bash
pytest tests/ -v --cov=. --cov-report=html
```

### Run Linting
```bash
flake8 . --max-line-length=120
```

### Run Type Checking
```bash
mypy . --ignore-missing-imports
```

---

## 🔧 Configuration

### Adjust Factory Specifications
Edit `factory_specs` in training notebook:
```python
factory_specs = {
    'conveyors': {'count': 14, 'max_power': 28},
    'pushers': {'count': 4, 'max_power': 12},
    'pick_place': {'count': 3, 'max_power': 12}
}
```

### Tune RL Hyperparameters
Modify in `02_rl_training.ipynb`:
```python
model = PPO(
    "MlpPolicy",
    vec_env,
    learning_rate=3e-4,
    batch_size=64,
    n_steps=2048,
    gamma=0.99
)
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Missing dependencies | `pip install --upgrade -r requirements.txt` |
| Jupyter not starting | `pip install --upgrade jupyter` |
| Streamlit port in use | `streamlit run app.py --server.port 8502` |
| Model training slow | Enable GPU: `pip install torch --index-url https://download.pytorch.org/whl/cu118` |

---

## 🚀 Future Enhancements

- [ ] Multi-agent RL for distributed control
- [ ] Real-time model retraining pipeline
- [ ] 3D factory visualization
- [ ] Predictive maintenance integration
- [ ] Time-of-use electricity rate optimization
- [ ] Advanced SCADA connectivity
- [ ] Cloud deployment support

---

## 📝 License

MIT License - see [LICENSE](LICENSE) for details

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/smart-energy-lader/issues)
- **Documentation**: See [docs/](docs/) folder
- **Examples**: Check [notebooks/](notebooks/) folder

---

## 🙏 Acknowledgments

- Stable-Baselines3 team for RL library
- Factory I/O for industrial simulation
- Streamlit for dashboard framework
- Our research team and contributors

---

<div align="center">

**Made with ⚡ by the Smart Energy Lader Team**

[⬆ back to top](#smart-energy-lader---ai-factory-optimization)

</div>
