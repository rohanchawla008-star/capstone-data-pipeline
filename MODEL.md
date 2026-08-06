# Machine Learning Model

## Objective

Predict whether a Titanic passenger survived based on passenger information.

---

## Problem Type

Binary Classification

- 0 → Did Not Survive
- 1 → Survived

---

## Features Used

- Passenger Class
- Sex
- Age
- Fare
- Siblings/Spouses
- Parents/Children
- Embarked Port

---

## Machine Learning Pipeline

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Feature Encoding
5. Model Training
6. Model Evaluation
7. Save Model
8. Deploy using Streamlit

---

## Model Serialization

The trained model is stored using Python Pickle and loaded by the Streamlit application for real-time predictions.

---

## Prediction Output

The application returns:

- Predicted Survival Status
- Survival Probability