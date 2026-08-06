import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/train_clean.csv")

print("Cleaned Dataset Loaded Successfully!")

# ----------------------------
# Encode Categorical Variables
# ----------------------------

# Male = 1, Female = 0
df["Sex"] = df["Sex"].map({
    "male": 1,
    "female": 0
})

# Embarked
df = pd.get_dummies(df, columns=["Embarked"], dtype=int)

# ----------------------------
# Normalize Fare
# ----------------------------

df["Fare"] = (
    (df["Fare"] - df["Fare"].min()) /
    (df["Fare"].max() - df["Fare"].min())
)

print("\nFirst 5 Rows After Transformation")
print(df.head())
# ----------------------------
# Feature Engineering
# ----------------------------

# Family Size
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Is Passenger Alone?
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Remove unnecessary columns
df = df.drop(columns=["PassengerId", "Name", "Ticket"])

print("\nFeature Engineering Completed!")

print(df.head())

# Save transformed dataset
df.to_csv("data/processed/train_transformed.csv", index=False)

print("\nTransformed dataset saved successfully!")

print("\nChecking for Outliers")

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Age"] < lower_bound) | (df["Age"] > upper_bound)]

print("Number of Age Outliers:", len(outliers))

print("\nVerifying Data Assumptions")

print("Minimum Age:", df["Age"].min())
print("Maximum Age:", df["Age"].max())

print("Minimum Fare:", df["Fare"].min())
print("Maximum Fare:", df["Fare"].max())
print("\nFinal Dataset Validation")

print("Dataset Shape:", df.shape)

print("Missing Values")
print(df.isnull().sum())

print("Duplicate Rows:", df.duplicated().sum())