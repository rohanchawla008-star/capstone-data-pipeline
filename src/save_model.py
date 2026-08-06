import pickle
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data/processed/train_transformed.csv")

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    max_depth=5,
    min_samples_split=2,
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
with open("models/model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully.")