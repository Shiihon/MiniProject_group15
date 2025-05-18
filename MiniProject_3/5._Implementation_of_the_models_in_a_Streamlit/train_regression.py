import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

BASE_DIR = os.path.dirname(__file__)

CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "another_cleaned_HR-Employee-Attrition.csv"))

df = pd.read_csv(CSV_PATH)
X = df[["Age", "JobLevel", "DistanceFromHome"]]
y = df["MonthlyIncome"]

model = LinearRegression().fit(X, y)

MODEL_PATH = os.path.join(BASE_DIR, "models", "regmodel.pkl")
joblib.dump(model, MODEL_PATH)
print(f"Saved regression model to {MODEL_PATH}")
