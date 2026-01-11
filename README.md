# Data Toolkit Final Project: Institutional Records

![Status](https://img.shields.io/badge/status-research--grade-green)
![Version](https://img.shields.io/badge/version-1.0-blue)

## 1. Overview
This is a capstone project for the **Data Toolkit** course. Its goal is to demonstrate a **reproducible (research-grade) data pipeline** that processes **synthetic institutional records**.

The project transforms raw data—containing **intentional errors** and **schema changes**—into a **clean, unified dataset** ready for analysis. The entire workflow is **version-controlled with Git** and **automated**.

## 2. Project Structure
```text
data_toolkit_project/
├── data/
│   ├── raw/             # Original data (IMMUTABLE)
│   └── processed/       # Clean outputs (CSV and Parquet)
├── docs/
│   ├── cli_notes.md     # Useful terminal commands
│   ├── checksums.sha256 # Integrity manifest
│   ├── data_dictionary.md
│   └── metadata.yaml
├── reports/             # Generated reports
├── src/
│   └── process_data.py  # Python cleaning script
├── Makefile             # Command automation
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## 3. Installation and Setup

### Requirements
- Python 3.8+
- Make (optional)

### Step 1: Clone and Install Dependencies
```bash
# 1. Clone the repository (if you don't already have it locally)
git clone <repo-url>
cd data_toolkit_project

# 2. Install Python dependencies
pip install -r requirements.txt
```

## 4. Running the Pipeline

### Automated (Make)
This command verifies data integrity, processes the dataset, and generates reports:
```bash
make all
```

To remove generated files and start from scratch:
```bash
make clean
```

### Manual (Python)
If you’re not using Make:
```bash
python3 src/process_data.py
```

## 5. Data Integrity and Documentation

### Verifying Raw Data
To prove the original data has not been corrupted or modified, run:
```bash
shasum -a 256 -c docs/checksums.sha256
```
*See `docs/integrity_notes.md` for details.*

### Output Formats
Processed data is saved in `data/processed/` in two formats:
1. **CSV**: For quick inspection and universal compatibility.
2. **Parquet**: For performance and preserved data types.

## 6. License and Contact
**Author:** Data Toolkit Student  
**License:** Educational Use Only  
**Version:** v1.0
