import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/processed/train_transformed.csv")

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Model
model = RandomForestClassifier(random_state=42)

# Parameters
parameters = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10],
    "min_samples_split": [2, 5, 10]
}

# Grid search
grid_search = GridSearchCV(
    estimator=model,
    param_grid=parameters,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# Training
grid_search.fit(X_train, y_train)

print("\nBest Parameters")
print(grid_search.best_params_)

print("\nBest Score")
print(grid_search.best_score_)