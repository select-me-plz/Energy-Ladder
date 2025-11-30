# Contributing to Smart Energy Lader

## Welcome!

Thank you for considering contributing to Smart Energy Lader! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Report unacceptable behavior to the team

## Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/smart-energy-lader.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install -e ".[dev]"
   ```

## Development Workflow

### Code Style
- Follow PEP 8 standards
- Use black for formatting: `black . --line-length=120`
- Use type hints where appropriate

### Testing
- Write tests for new features
- Ensure all tests pass: `pytest tests/ -v`
- Maintain >80% code coverage

### Documentation
- Document functions with docstrings
- Update README.md if needed
- Add examples for new features

### Commit Messages
```
[TYPE] Brief description

Longer explanation if needed.

Fixes #ISSUE_NUMBER
```

Types: feat, fix, docs, style, refactor, test, chore

## Pull Request Process

1. **Update your branch** with latest main
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run quality checks**
   ```bash
   make lint
   make test
   ```

3. **Create pull request** with:
   - Clear title and description
   - Reference to related issue
   - List of changes made
   - Screenshots/videos if UI changes

4. **Respond to reviews** and iterate

5. **Get approval** and merge

## Reporting Issues

### Bug Reports
Include:
- Python version and OS
- Reproduction steps
- Expected vs actual behavior
- Error messages and traceback
- Environment details

### Feature Requests
Include:
- Clear description of feature
- Why it would be useful
- Potential implementation approach
- Examples or mockups

## Development Tips

- **Local testing**: `python demo_script.py`
- **Dashboard testing**: `streamlit run dashboard/app.py`
- **Notebook testing**: `jupyter notebook`
- **Debug mode**: Add print statements or use pdb

## Areas for Contribution

- **Core Features**: RL algorithms, environment improvements
- **Integration**: Factory I/O, LabVIEW, SCADA connectors
- **Dashboard**: UI/UX improvements, new visualizations
- **Documentation**: Examples, guides, API docs
- **Testing**: Unit tests, integration tests, performance tests
- **DevOps**: CI/CD improvements, deployment scripts

## Questions?

- Check existing issues and discussions
- Review documentation in `docs/`
- Look at example notebooks
- Reach out to the team

## Thank You!

Your contributions help make Smart Energy Lader better for everyone. We appreciate your time and effort!

---

**Happy Contributing!**
