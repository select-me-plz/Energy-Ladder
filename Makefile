# Smart Energy Lader - Makefile

.PHONY: help install run-dashboard run-demo test clean lint format docs

help:
	@echo "Smart Energy Lader - Available Commands"
	@echo "========================================"
	@echo "make install          - Install dependencies"
	@echo "make run-dashboard    - Run Streamlit dashboard"
	@echo "make run-demo         - Run complete demo"
	@echo "make run-notebook     - Run Jupyter notebook"
	@echo "make test             - Run test suite"
	@echo "make lint             - Run linting checks"
	@echo "make format           - Format code with black"
	@echo "make clean            - Remove cache and build files"
	@echo "make docs             - Build documentation"

install:
	pip install -r requirements.txt
	pip install -r dashboard/requirements.txt

run-dashboard:
	streamlit run dashboard/app.py

run-demo:
	python demo_script.py

run-notebook:
	jupyter notebook notebooks/

test:
	pytest tests/ -v --cov=. --cov-report=html

lint:
	flake8 . --max-line-length=120
	mypy . --ignore-missing-imports

format:
	black . --line-length=120

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage

docs:
	@echo "Building documentation..."
	@echo "See docs/ folder for documentation"

.DEFAULT_GOAL := help
