#!/bin/bash

# Activate the virtual environment
if ! source env/bin/activate; then
  echo "Failed to activate virtual environment"
  exit 1
fi

# Navigate to the src directory
if ! cd src; then
  echo "Failed to change directory to src"
  exit 1
fi

# Run the Streamlit app
if ! streamlit run main.py; then
  echo "Failed to run Streamlit app"
  exit 1
fi
