#!/bin/bash

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate  # For macOS/Linux
# venv\Scripts\activate     # Uncomment for Windows

# Check if the Lambda function script exists
if [ ! -f lambda_function.py ]; then
    echo "Error: lambda_function.py not found!"
    exit 1
fi

# Run the Lambda function
echo "Running the Lambda function..."
python lambda_function.py

# Check the exit status of the previous command
if [ $? -eq 0 ]; then
    echo "Lambda function executed successfully."
else
    echo "Error: Lambda function execution failed."
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Run completed."
