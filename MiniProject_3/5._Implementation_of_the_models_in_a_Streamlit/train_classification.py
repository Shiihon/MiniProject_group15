import os
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import joblib

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "another_cleaned_HR-Employee-Attrition.csv"))

df = pd.read_csv(CSV_PATH)
df["OverTimeNum"] = (df["OverTime"] == "Yes").astype(int)

X = df[["Age", "DistanceFromHome", "JobLevel", "OverTimeNum", "TrainingTimesLastYear"]]
y = (df["Attrition"] == "Yes").astype(int)

clf = GaussianNB().fit(X, y)

MODEL_PATH = os.path.join(BASE_DIR, "models", "nbmodel.pkl")
joblib.dump(clf, MODEL_PATH)
print(f"Saved classification model to {MODEL_PATH}")
