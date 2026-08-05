# Titanic Data Pipeline Capstone Project

This repository contains my CodeZoner Capstone Internship project. The objective of this project is to build a complete data pipeline using the Titanic dataset, including data loading, preprocessing, exploratory data analysis, feature engineering, visualization, and pipeline automation.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- Scikit-learn
- Git
- GitHub

---

## Features

- Data ingestion pipeline
- Data validation
- Logging and exception handling
- Data cleaning
- Feature engineering
- Data transformation
- Data visualization
- Correlation analysis
- Outlier detection
- Pipeline automation
- SQLite integration
- Git version control

---

## Project Structure

```text
CodeZoner_Capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
├── notebooks/
├── reports/
│
├── src/
│   ├── database.py
│   ├── eda.py
│   ├── load_data.py
│   ├── transform_data.py
│   ├── visualization.py
│   └── pipeline.py
│
├── cloud_storage/
├── .env
├── .env.example
├── .gitignore
├── database.db
├── titanic.db
├── requirements.txt
├── README.md
├── PROJECT_PLAN.md
├── test_setup.py
└── Titanic_EDA.ipynb
```

---

## Data Source

### Primary Dataset

- Titanic dataset (CSV)
- Source: Kaggle Titanic Competition
- Access method: Local CSV file using Pandas

```python
df = pd.read_csv("data/raw/train.csv")
```

### Data Limitations

- Missing values in Age
- Missing values in Cabin
- Missing values in Embarked
- Static dataset
- No real-time data source

### Future Improvements

- Kaggle API integration
- REST API integration
- Cloud storage integration
- SQL database integration

---

## Week 1 Progress ✅

### Completed Tasks

- Created repository
- Configured virtual environment
- Installed required libraries
- Loaded the Titanic dataset
- Handled missing values
- Created a cleaned dataset
- Performed exploratory data analysis
- Updated GitHub repository

### Status

Week 1 Completed ✅

---

## Week 2 Progress ✅

### Completed Tasks

- Explored data sources
- Implemented data ingestion pipeline
- Added error handling
- Created SQLite database
- Stored and retrieved Titanic data
- Added validation checks
- Processed missing values
- Saved cleaned datasets

### Status

Week 2 Completed ✅

---

## Week 3 Progress ✅

### Completed Tasks

- Standardized numerical features
- Encoded categorical variables
- Created FamilySize feature
- Created IsAlone feature
- Generated distribution plots
- Created correlation heatmaps
- Performed outlier detection
- Verified dataset quality
- Built preprocessing pipeline
- Split data into training and testing sets
- Applied feature scaling

### Status

Week 3 Completed ✅

---

## Week 4 Progress ✅

### Day 22 – Data Ingestion

- Loaded the dataset
- Added logging
- Implemented exception handling
- Performed validation checks

### Day 23 – Data Processing

- Handled missing values
- Encoded categorical features
- Normalized numerical features
- Applied feature engineering

### Day 24 – Data Visualization

- Created age distribution plots
- Generated correlation heatmaps
- Performed visualization checks

### Day 25 – Pipeline Integration

- Integrated all modules
- Executed the complete pipeline
- Added monitoring and validation
- Refactored the code

### Day 26 – Review and GitHub

- Fixed bugs
- Updated documentation
- Uploaded changes to GitHub

### Status

Week 4 Completed ✅

---

## Running the Project

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Run the complete pipeline

```bash
python src/pipeline.py
```

---

## Output Files

```text
data/processed/train_clean.csv
data/processed/train_transformed.csv
database.db
```

---

## Upcoming Work

- Machine learning model development
- Model training
- Model evaluation
- Performance optimization
- Final documentation

---

## Author

Rohan Chawla

CodeZoner Capstone Internship Project