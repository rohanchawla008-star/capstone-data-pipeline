import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/train_clean.csv")

print("First 5 Rows")
print(df.head())

print("\nStatistical Summary")
print(df.describe())

print("\nSurvival Count")
print(df["Survived"].value_counts())

print("\nPassenger Class Count")
print(df["Pclass"].value_counts())

print("\nGender Count")
print(df["Sex"].value_counts())