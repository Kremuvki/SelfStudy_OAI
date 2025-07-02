#!/bin/bash

# Enhanced setup script for SelfStudy_OAI
# Handles different architectures and provides better error reporting

set -e  # Exit on any error

echo "🚀 Starting SelfStudy_OAI setup..."

# Check if we're on macOS and detect architecture
if [[ "$OSTYPE" == "darwin"* ]]; then
    ARCH=$(uname -m)
    echo "📱 Detected macOS with architecture: $ARCH"
    
    # On Apple Silicon, prefer system Python to avoid SSL issues
    if [[ "$ARCH" == "arm64" ]]; then
        echo "🍎 Apple Silicon detected - using system Python for better compatibility"
        PYTHON_CMD="/usr/bin/python3"
        if [[ ! -f "$PYTHON_CMD" ]]; then
            echo "❌ System Python not found. Please install Python through Xcode Command Line Tools:"
            echo "   xcode-select --install"
            exit 1
        fi
    else
        PYTHON_CMD="python3"
    fi
else
    PYTHON_CMD="python3"
fi

# Check Python version
echo "🐍 Checking Python version..."
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
echo "   Found Python $PYTHON_VERSION"

# Check if Python version is 3.8 or higher
if $PYTHON_CMD -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "✅ Python version is sufficient (3.8+)"
else
    echo "❌ Python 3.8+ is required. Found: $PYTHON_VERSION"
    exit 1
fi

# Remove existing virtual environment if it exists
if [[ -d "venv" ]]; then
    echo "🧹 Removing existing virtual environment..."
    rm -rf venv
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Test SSL functionality
echo "🔒 Testing SSL functionality..."
if python -c "import ssl; print('SSL working')" 2>/dev/null; then
    echo "✅ SSL is working correctly"
else
    echo "❌ SSL issues detected. This may cause package installation problems."
    echo "   On macOS with Apple Silicon, this script already uses system Python."
    echo "   You may need to reinstall Python or use conda instead."
fi

# Upgrade pip
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies with retry logic
echo "📚 Installing dependencies..."
if pip install -r requirements.txt; then
    echo "✅ All dependencies installed successfully"
else
    echo "⚠️  Some packages failed to install. Trying individual installation..."
    
    # Core packages
    echo "📊 Installing core scientific packages..."
    pip install numpy pandas scikit-learn matplotlib seaborn
    
    # Jupyter
    echo "📓 Installing Jupyter..."
    pip install jupyter notebook
    
    # Development tools
    echo "🛠️  Installing development tools..."
    pip install pytest black isort flake8
    
    # Try nbqa separately as it sometimes fails
    echo "📋 Installing notebook quality tools..."
    pip install nbqa || echo "⚠️  nbqa installation failed - you can install it later"
    
    # Pre-commit hooks
    echo "🎣 Installing pre-commit..."
    pip install pre-commit || echo "⚠️  pre-commit installation failed - you can install it later"
fi

# Create data directory if it doesn't exist
echo "📁 Setting up data directory..."
mkdir -p data
touch data/.gitkeep

# Run basic tests
echo "🧪 Running basic tests..."
if python -c "import numpy, pandas; print('✅ Core packages working')"; then
    echo "✅ Basic package imports successful"
else
    echo "❌ Basic package imports failed"
    exit 1
fi

echo "🔧 Setting up Jupyter kernel..."
python -m ipykernel install --user --name=selfstudy-oai --display-name="SelfStudy OAI"

echo "🎯 Testing basic imports..."
python -c "import torch, torchvision, cv2, nltk, tqdm, PIL, numpy, pandas, sklearn, matplotlib, seaborn, jupyter; print('✅ All packages working!')" || {
    echo "❌ Some packages failed to import. Please check the installation."
    exit 1
}

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Start Jupyter: jupyter notebook"
echo "3. Select 'SelfStudy OAI' kernel when creating/opening notebooks"
echo ""
echo "💡 Available Jupyter kernels:"
jupyter kernelspec list | grep -E "(selfstudy-oai|python3|SelfStudy)" || echo "   Run 'jupyter kernelspec list' to see all kernels"
echo ""
echo "🧪 Run tests: pytest tests/ -v" 