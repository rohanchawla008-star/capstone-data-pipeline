import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load transformed dataset
df = pd.read_csv("data/processed/train_transformed.csv")

print("Dataset Loaded Successfully!\n")

# Features and Target
X = df.drop("Survived", axis=1)
y = df["Survived"]

print("Features Shape:", X.shape)
print("Target Shape:", y.shape)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain-Test Split Completed!")

print("Training Samples:", X_train.shape)
print("Testing Samples:", X_test.shape)

# Scale Numerical Columns
scaler = StandardScaler()

numerical_columns = ["Age", "Fare", "FamilySize"]

X_train[numerical_columns] = scaler.fit_transform(
    X_train[numerical_columns]
)

X_test[numerical_columns] = scaler.transform(
    X_test[numerical_columns]
)

print("\nFeature Scaling Completed!")

print("\nPipeline Executed Successfully!")