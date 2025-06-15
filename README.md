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

- Use `black` for code formatting
- Use `isort` for import sorting
- Use `flake8` for linting
- Run tests with `pytest`

## License

MIT License - see LICENSE file for details 