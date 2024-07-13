#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate  # For macOS/Linux

# Check if config.toml exists
if [ -f config.toml ]; then
    echo "Configuration file config.toml found."
else
    echo "Error: config.toml file not found. Please create this file to provide necessary configuration."
    exit 1  # Exit the script with an error
fi

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Load environment variables
if [ -f .env ]; then
    echo "Loading environment variables from .env..."
    export $(grep -v '^#' .env | xargs)
else
    echo ".env file not found."
fi

echo "Initialization complete."
