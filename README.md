# Self-Study OAI

A collection of machine learning competition solutions and exercises, focusing on practical implementations and best practices.

## 📋 Overview

This repository contains 6 different machine learning problems with complete solutions and tutorials:

1. **Adversarial Attacks** - Neural network security and robustness
2. **Color Quantization** - Image processing and clustering
3. **Dependency Parsing** - Natural language processing
4. **Imbalanced Classification** - Handling skewed datasets
5. **Neural Network Pruning** - Model compression techniques
6. **Word Riddles** - Text analysis and pattern recognition

## 📁 Project Structure

```
├── .github/                    # CI/CD pipelines
├── data/                       # Central data storage
├── problems/                   # Competition tasks
│   ├── 01_adversarial_attacks/
│   │   ├── problem/            # Problem statement
│   │   ├── solution/           # Complete solution
│   │   └── tutorial/           # Learning materials
│   ├── 02_color_quantization/
│   └── ... (other problems)
├── scripts/                    # Utility scripts
├── tests/                      # Unit/integration tests
├── requirements.txt           # Python dependencies
├── environment.yml            # Conda environment
└── pyproject.toml            # Project configuration
```

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd SelfStudy_OAI

# Run the setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Activate the environment
source venv/bin/activate
```

### Option 2: Manual Setup with pip

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Using Conda

```bash
# Create and activate conda environment
conda env create -f environment.yml
conda activate selfstudy_oai
```

## 🔧 System Requirements

- **Python**: 3.8 or higher
- **OS**: macOS, Linux, or Windows
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 2GB free space

### Platform-Specific Notes

#### macOS (Apple Silicon)
- The setup script automatically detects Apple Silicon and uses system Python to avoid SSL issues
- If you encounter SSL problems, try using conda instead of pip
- Xcode Command Line Tools are required: `xcode-select --install`

#### macOS (Intel)
- Standard Python installation should work fine
- Both pip and conda options are supported

#### Linux
- Most distributions work out of the box
- Ensure you have `python3-venv` installed: `sudo apt install python3-venv`

#### Windows
- Use PowerShell or Command Prompt
- Replace `source venv/bin/activate` with `venv\Scripts\activate`

## 🧪 Testing

Run the test suite to ensure everything is working:

```bash
# Activate environment first
source venv/bin/activate

# Run all tests
pytest tests/

# Run specific test
pytest tests/test_basic.py -v

# Run tests with coverage
pytest tests/ --cov=.
```

## 💻 Development Workflow

### Code Quality Tools

The project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting  
- **flake8**: Linting
- **nbqa**: Apply tools to Jupyter notebooks
- **pytest**: Testing

### Running Quality Checks

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
```

### Pre-commit Hooks (Optional)

For automatic code formatting on commit:

```bash
pip install pre-commit
pre-commit install
```

## 📚 Working with Notebooks

### Starting Jupyter

```bash
# Activate environment
source venv/bin/activate

# Start Jupyter Lab (recommended)
jupyter lab

# Or start classic Jupyter Notebook
jupyter notebook
```

**⚠️ Important**: When opening any notebook, make sure to select the **"SelfStudy OAI"** kernel from the kernel dropdown menu (Kernel → Change Kernel → SelfStudy OAI). This ensures all required packages (PyTorch, OpenCV, NLTK, tqdm, etc.) are available.

### Notebook Organization

Each problem follows this structure:
- **Problem notebook**: Contains the task description and starter code
- **Solution notebook**: Complete working solution  
- **Tutorial notebook**: Step-by-step explanation and learning materials

### Data Management

- Data is automatically downloaded when running problem notebooks
- All data is stored in the `data/` directory
- Each notebook handles its own data dependencies

## 🔍 Troubleshooting

### Common Issues

#### SSL Certificate Errors
**Problem**: `SSL: CERTIFICATE_VERIFY_FAILED` or similar SSL errors

**Solutions**:
1. On macOS with Apple Silicon: Use the automated setup script
2. Try using conda instead of pip: `conda env create -f environment.yml`
3. Update certificates: `pip install --upgrade certifi`

#### Package Installation Failures
**Problem**: Some packages fail to install

**Solutions**:
1. Update pip: `pip install --upgrade pip`
2. Install packages individually: `pip install numpy pandas scikit-learn`
3. Try using conda: `conda install numpy pandas scikit-learn`
4. Clear pip cache: `pip cache purge`

#### Architecture Mismatch (macOS)
**Problem**: Library architecture incompatibility

**Solutions**:
1. Use the automated setup script which detects architecture
2. Use system Python: `/usr/bin/python3 -m venv venv`
3. Reinstall Python for your architecture from python.org

#### Jupyter Kernel Issues
**Problem**: Jupyter can't find the virtual environment

**Solutions**:
1. Install ipykernel: `pip install ipykernel`
2. Add environment to Jupyter: `python -m ipykernel install --user --name=selfstudy_oai`
3. Restart Jupyter and select the correct kernel

### Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Run the setup script with verbose output: `bash -x scripts/setup.sh`
3. Verify your Python installation: `python --version`
4. Check virtual environment: `which python` (should point to venv)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests and quality checks
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use Black for formatting
- Add docstrings to functions
- Write tests for new features

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Competition problems inspired by OAI (Olimpiada Algorytmów i Inteligencji Sztucznej)
- Reference implementations and tutorials created for educational purposes
- Thanks to all contributors and the machine learning community

---

**Happy Learning! 🎓** 