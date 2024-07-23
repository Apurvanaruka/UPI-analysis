#!/bin/bash

DIRECTORY="env"

if [ -d "$DIRECTORY" ]; then
  # Activate the virtual environment
  echo "activating virtual environment"
  if ! source env/bin/activate; then
    echo "Failed to activate virtual environment"
    exit 1
  fi
  echo "installing dependencies"
  if ! pip3 install -r requirements.txt; then
    echo "Faild to install dependenicies"
  fi
  echo "change dir to src folder"
  # Navigate to the src directory
  if ! cd src; then
    echo "Failed to change directory to src"
    exit 1
  fi
  echo "Run the Streamlit app"
  # Run the Streamlit app
  if ! streamlit run main.py; then
    echo "first"
    echo "Failed to run Streamlit app"
    exit 1
  fi

else
  echo "Creating virtual ennvirnment"
  if ! python3 -m venv env; then 
    echo "Failed to create virtural env"
  fi
  # Activate the virtual environment
  echo "Activate the virtual environment"
  if ! source env/bin/activate; then
    echo "Failed to activate virtual environment"
    exit 1
  fi
  echo "installing dependencies"
  if ! pip3 install -r requirements.txt; then
    echo "Faild to install dependicies"
  fi

  # Navigate to the src directory
  echo "Navigate to the src directory"
  if ! cd src; then
    echo "Failed to change directory to src"
    exit 1
  fi

  # Run the Streamlit app
  echo "Run the Streamlit app"
  if ! streamlit run main.py; then
    echo "Failed to run Streamlit app"
    exit 1
  fi

fi

