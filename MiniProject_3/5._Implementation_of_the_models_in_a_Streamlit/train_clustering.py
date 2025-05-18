import os
import pandas as pd
from sklearn.cluster import KMeans
import joblib

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "another_cleaned_HR-Employee-Attrition.csv"))

df = pd.read_csv(CSV_PATH)
features = ["Age", "MonthlyIncome", "DistanceFromHome"]
X = df[features]

km = KMeans(n_clusters=4, random_state=42).fit(X)

MODEL_PATH = os.path.join(BASE_DIR, "models", "cluster_model.pkl")
joblib.dump(km, MODEL_PATH)
print(f"Saved clustering model to {MODEL_PATH}")
