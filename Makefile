# Variables
PYTHON = python3
PIP = pip

.PHONY: all setup clean run

# Default target
all: setup run

# Setup environment
setup:
	$(PIP) install -r requirements.txt

# Run the pipeline
run:
	$(PYTHON) src/process_data.py

# Clean generated files
clean:
	rm -f data/processed/*
	rm -f reports/*