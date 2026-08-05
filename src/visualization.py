import pandas as pd
import matplotlib.pyplot as plt

# Load transformed dataset
df = pd.read_csv("data/processed/train_transformed.csv")

print("Dataset Loaded Successfully!")

# -----------------------------
# Distribution of Age
# -----------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------

correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix")
print(correlation)

# -----------------------------
# Heatmap
# -----------------------------

plt.figure(figsize=(10,8))

plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()

print("\nVisualization Completed Successfully!")