import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
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

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column
df.drop(columns=["Cabin"], inplace=True)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("data/processed/train_clean.csv", index=False)

print("\nCleaned dataset saved successfully!")