# Self-Study OAI

A collection of machine learning competition solutions and exercises, focusing on practical implementations and best practices.

## Project Structure

```
├── .github/                    # CI/CD pipelines
├── data/                       # Central data storage
├── problems/                   # Competition tasks
│   ├── 01_adversarial_attacks/
│   ├── 02_color_quantization/
│   └── ... (other problems)
├── scripts/                    # Utility scripts
├── tests/                      # Unit/integration tests
└── ... (configuration files)
```

## Setup

### Using pip

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Using Conda

```bash
# Create and activate conda environment
conda env create -f environment.yml
conda activate selfstudy_oai
```

## Development

### Code Quality Tools

- Use `black` for code formatting (Python files and notebooks)
- Use `isort` for import sorting (Python files and notebooks)
- Use `flake8` for linting (Python files and notebooks)
- Use `nbqa` to apply these tools to Jupyter notebooks
- Run tests with `pytest`

### Commands

```bash
# Format code
black .
nbqa black .

# Sort imports
isort .
nbqa isort .

# Lint code
flake8 .
nbqa flake8 .

# Run all quality checks
black . --check && nbqa black . --check && \
isort . --check-only && nbqa isort . --check-only && \
flake8 . && nbqa flake8 .

# Run tests
pytest tests/
```

### Pre-commit Setup (Optional)

For automatic code formatting on commit, install pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

## License

MIT License - see LICENSE file for details 