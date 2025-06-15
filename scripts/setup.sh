#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create data directory if it doesn't exist
mkdir -p data

# Create .gitkeep in data directory
touch data/.gitkeep

echo "Setup complete! Don't forget to activate the virtual environment with:"
echo "source venv/bin/activate" 