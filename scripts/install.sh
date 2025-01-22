#!/bin/bash

# Installation script for ItsFyn

echo "Starting ItsFyn installation..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Detected Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating project directories..."
mkdir -p logs
mkdir -p config
mkdir -p data

# Copy default configuration
echo "Setting up configuration..."
cp config/default_config.json config/config.json

echo "Installation complete!"
