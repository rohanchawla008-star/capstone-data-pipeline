import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/processed/train_transformed.csv")

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Cross-validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\nCross-Validation Scores\n")

for index, score in enumerate(scores, start=1):
    print(f"Fold {index}: {score:.4f}")

print("\nAverage Accuracy:", round(scores.mean(), 4))