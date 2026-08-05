# Titanic Data Pipeline Capstone Project

This repository contains my CodeZoner Capstone Internship project. The goal of this project is to build a complete machine learning pipeline using the Titanic dataset, including data ingestion, preprocessing, feature engineering, visualization, model training, evaluation, optimization, and interpretation.

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
- Machine learning model training
- Model evaluation
- Cross-validation
- Hyperparameter optimization
- Feature importance analysis

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
│   ├── cross_validation.py
│   ├── database.py
│   ├── eda.py
│   ├── load_data.py
│   ├── model_evaluation.py
│   ├── model_interpretation.py
│   ├── model_optimization.py
│   ├── model_selection.py
│   ├── model_training.py
│   ├── pipeline.py
│   ├── transform_data.py
│   └── visualization.py
│
├── .env
├── .env.example
├── .gitignore
├── database.db
├── titanic.db
├── README.md
├── requirements.txt
├── PROJECT_PLAN.md
├── test_setup.py
└── Titanic_EDA.ipynb
```

---

# Data Source

### Primary Dataset

- Titanic Dataset
- Source: Kaggle Titanic Competition
- Format: CSV

```python
df = pd.read_csv("data/raw/train.csv")
```

---

## Dataset Limitations

- Missing values in Age
- Missing values in Cabin
- Missing values in Embarked
- Static dataset
- No real-time updates

---

# Week 1 Progress

### Completed Tasks

- Repository created
- Virtual environment configured
- Required libraries installed
- Titanic dataset loaded
- Missing values handled
- Exploratory data analysis completed
- Processed dataset generated

### Status

✅ Week 1 Completed

---

# Week 2 Progress

### Completed Tasks

- Implemented the data ingestion pipeline
- Added logging functionality
- Added exception handling
- Created SQLite database integration
- Added validation checks
- Cleaned missing values
- Saved processed dataset

### Status

✅ Week 2 Completed

---

# Week 3 Progress

### Completed Tasks

- Standardized numerical variables
- Encoded categorical variables
- Created FamilySize feature
- Created IsAlone feature
- Generated visualizations
- Performed outlier detection
- Split training and testing datasets
- Applied feature scaling

### Status

✅ Week 3 Completed

---

# Week 4 Progress

### Day 22 — Data Ingestion

- Loaded Titanic dataset
- Added logging
- Implemented exception handling
- Performed validation checks

### Day 23 — Data Processing

- Cleaned missing values
- Encoded categorical variables
- Normalized features
- Performed feature engineering

### Day 24 — Data Visualization

- Created histograms
- Generated correlation heatmaps
- Performed data analysis

### Day 25 — Pipeline Integration

- Integrated all components
- Executed the complete pipeline
- Performed testing

### Status

✅ Week 4 Completed

---

# Week 5 Progress

## Model Selection

Selected models:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

---

## Model Training Results

| Model | Accuracy |
|------|------|
| Logistic Regression | 80.45% |
| Decision Tree | 79.89% |
| Random Forest | 82.68% |
| KNN | 78.77% |

---

## Model Evaluation

| Metric | Score |
|------|------|
| Accuracy | 82.68% |
| Precision | 80.28% |
| Recall | 77.03% |
| F1 Score | 78.62% |

---

## Confusion Matrix

```text
[[91 14]
 [17 57]]
```

---

## Cross-Validation Results

| Fold | Accuracy |
|------|------|
| Fold 1 | 75.98% |
| Fold 2 | 79.78% |
| Fold 3 | 87.08% |
| Fold 4 | 78.65% |
| Fold 5 | 82.02% |

Average accuracy:

```text
80.70%
```

---

## Hyperparameter Optimization

Best parameters:

```python
{
    "max_depth": 5,
    "min_samples_split": 2,
    "n_estimators": 100
}
```

Best score:

```text
82.86%
```

---

## Feature Importance

| Feature | Importance |
|------|------:|
| Sex | 0.4256 |
| Fare | 0.1662 |
| Pclass | 0.1252 |
| Age | 0.0960 |
| FamilySize | 0.0700 |

---

## Running the Project

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run the pipeline:

```bash
python src/pipeline.py
```

Run model training:

```bash
python src/model_training.py
```

Run model evaluation:

```bash
python src/model_evaluation.py
```

Run cross-validation:

```bash
python src/cross_validation.py
```

Run model optimization:

```bash
python src/model_optimization.py
```

Run model interpretation:

```bash
python src/model_interpretation.py
```

---

## Current Status

✅ Week 1 Completed

✅ Week 2 Completed

✅ Week 3 Completed

✅ Week 4 Completed

✅ Week 5 Completed

🚀 Week 6 Coming Soon