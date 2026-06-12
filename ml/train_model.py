import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("../dataset/train.csv", encoding="utf-8")

# Features + target
X = df.iloc[:, :11]
y = df["FloodProbability"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model to backend
joblib.dump(model, "../backend/model.pkl")

print("Model trained and saved successfully!")