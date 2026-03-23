# 🏥 Medical Data Quality Pipeline

A modular and scalable **medical data quality pipeline** built in Python to automate cleaning, validation, and profiling of real-world healthcare datasets. Designed to ensure data reliability and consistency for analytics, reporting, and machine learning tasks in the medical domain.

---

## 🚀 Overview

Healthcare datasets are often messy, incomplete, and inconsistent. This project provides a structured pipeline to process raw medical datasets and transform them into **high-quality, analysis-ready data**.

The pipeline follows a standard ETL approach:

- **Extract** → Load raw medical data  
- **Transform** → Clean and validate data  
- **Load** → Output processed datasets and reports  

---

## ⚙️ Features

### Data Cleaning
- Handle missing values  
- Remove duplicates  
- Standardize medical and numeric data formats  

### Data Validation
- Schema validation  
- Rule-based checks (e.g., valid ranges, medical thresholds)  

### Data Profiling
- Summary statistics  
- Distribution analysis  
- Missing value analysis  

### Outlier Detection
- Statistical methods (IQR, Z-score)

### Reporting
- Automated generation of **data quality reports**  
- Visualizations for better understanding  

---

## 🏗️ Project Structure

```
medical-data-quality-pipeline/
│
├── data/
│   ├── raw/         # Original datasets (unchanged)
│   └── processed/   # Cleaned datasets
│
├── src/             # Core pipeline modules
│   ├── cleaning.py
│   ├── validation.py
│   └── profiling.py
│
├── notebooks/       # Exploratory analysis
│   └── demo_analysis.ipynb
│
├── spss_workflow/   # SPSS Modeler workflow & reports
│   ├── workflow.str
│   └── report.pdf
│
├── reports/         # Final generated reports
│   └── combined_report.pdf
│
├── config/          # Configuration files
│   └── validation_rules.json
│
├── requirements.txt
└── README.md
```

---

## 🎯 Objectives

- Improve data quality for medical analytics  
- Automate repetitive medical data preparation tasks  
- Provide clear insights into **dataset health**  
- Ensure datasets are ready for **analytics and ML in healthcare**  

---

## 🔄 Workflow

1. Load raw dataset (CSV, relational tables, or demo data)  
2. Apply cleaning operations (missing values, duplicates, invalid entries)  
3. Validate data using predefined rules (medical thresholds, timestamps, ranges)  
4. Perform data profiling and analysis  
5. Generate reports and export cleaned dataset  

---

## 🧩 Recommended Dataset

**MIMIC-IV-ED Demo** – Open-access subset of real hospital data:

- 100 patient records  
- Tables: `edstays`, `diagnosis`, `triage`, `vitalsign`, `medrecon`, `pyxis`  
- Perfect for testing cleaning, validation, and profiling pipelines  

> Start small with the demo and scale to full MIMIC-IV for a professional, CV-worthy project.

---

## 🔧 Getting Started

### 1. Download dataset

**Manual download (Windows-friendly)**:  
[Download ZIP (95.5 KB)](https://physionet.org/files/mimic-iv-ed-demo/2.2/)  
Extract and move files into:

```bash
data/raw/
```

### 2. Explore the dataset

```python
import pandas as pd

edstays = pd.read_csv("data/raw/edstays.csv")
print(edstays.head())
print(edstays.info())
print(edstays.isnull().sum())
```

### 3. Apply pipeline

- Clean missing values and duplicates  
- Validate numeric and categorical columns  
- Profile dataset and generate reports  

---

## 🧩 Future Enhancements

- Interactive dashboard (Streamlit)  
- SQL/database integration  
- API-based data ingestion  
- Advanced anomaly detection (ML-based)  

---

## 📌 Status

🚧 Project initialized — development in progress.  

> Tested on **MIMIC-IV-ED Demo** and designed to scale to full MIMIC-IV datasets.
