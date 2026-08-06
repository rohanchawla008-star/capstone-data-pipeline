import pandas as pd
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Load dataset
    df = pd.read_csv("data/raw/train.csv")
    logging.info("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: train.csv not found.")
    exit()

except Exception as e:
    print(f"Unexpected Error: {e}")
    exit()

# -----------------------------
# Data Validation
# -----------------------------

logging.info(f"Dataset Shape: {df.shape}")

logging.info("Checking Missing Values...")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column
df = df.drop(columns=["Cabin"])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nData Types After Cleaning")
print(df.dtypes)

print("\nChecking for Duplicate Rows")

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("data/processed/train_clean.csv", index=False)

logging.info("Cleaned dataset saved successfully.")

# Validate dataset

required_columns = [
    "PassengerId",
    "Survived",
    "Pclass",
    "Name",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Ticket",
    "Fare",
    "Embarked"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print("Missing Columns:", missing_columns)
    exit()

logging.info("Dataset validation successful.")
print("\nData Types After Cleaning")
print(df.dtypes)

print("\nChecking for Duplicate Rows")
duplicates = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

if duplicates == 0:
    print("No duplicate rows found.")
else:
    print("Duplicate rows detected.")