import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/train.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column
df = df.drop(columns=["Cabin"])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("data/processed/train_clean.csv", index=False)

print("\nCleaned dataset saved successfully!")