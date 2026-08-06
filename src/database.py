import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("titanic.db")

# Load cleaned dataset
df = pd.read_csv("data/processed/train_clean.csv")

# Store dataset into SQLite
df.to_sql(
    "titanic",
    conn,
    if_exists="replace",
    index=False
)

# Retrieve data from database
result = pd.read_sql("SELECT * FROM titanic LIMIT 5", conn)

print("First 5 Rows From Database")
print(result)

conn.close()