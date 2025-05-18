import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_option_menu import option_menu


st.set_page_config(page_title="HR Attrition Task 5", page_icon="💼", layout="wide")


BASE_DIR = os.path.dirname(__file__)
MINI3_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_PATH = os.path.join(MINI3_DIR, "data", "another_cleaned_HR-Employee-Attrition.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")


def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"Could not find dataset at {path}")
        st.stop()

def load_model(fname):
    p = os.path.join(MODELS_DIR, fname)
    if not os.path.exists(p):
        st.error(f"Model not found: {p}")
        st.stop()
    return joblib.load(p)

@st.cache_data
def get_data():
    return load_data(DATA_PATH)

df = get_data()

choice = option_menu(
    menu_title="Choose Model",
    options=["Income Regression", "Attrition Classification", "Clustering"],
    icons=["currency-pound", "person-x-fill", "layers-fill"],
    menu_icon="cast",
    default_index=0,
)

if choice == "Income Regression":
    st.header("Income Regression")
    st.write("Predict monthly income using regression model.")
    m = load_model("regmodel.pkl")
    age = st.number_input("Age", int(df.Age.min()), int(df.Age.max()), int(df.Age.median()))
    joblevel = st.selectbox("Job Level", sorted(df.JobLevel.unique()))
    distance = st.number_input("Distance From Home", int(df.DistanceFromHome.min()), int(df.DistanceFromHome.max()), int(df.DistanceFromHome.median()))
    if st.button("Predict Income"):
        st.write(f"Monthly Income: {m.predict([[age, joblevel, distance]])[0]:.2f}")

elif choice == "Attrition Classification":
    st.header("Attrition Classification")
    st.write("Predict whether an employee will leave.")
    m = load_model("nbmodel.pkl")
    age = st.slider("Age", int(df.Age.min()), int(df.Age.max()), int(df.Age.median()))
    distance = st.slider("Distance From Home", int(df.DistanceFromHome.min()), int(df.DistanceFromHome.max()), int(df.DistanceFromHome.median()))
    overtime = st.radio("OverTime", ("Yes", "No"))
    joblevel = st.selectbox("Job Level", sorted(df.JobLevel.unique()))
    training = st.number_input("Training Times Last Year", int(df.TrainingTimesLastYear.min()), int(df.TrainingTimesLastYear.max()), int(df.TrainingTimesLastYear.median()))
    if st.button("Predict Attrition"):
        val = [age, distance, joblevel, 1 if overtime=="Yes" else 0, training]
        st.write("Will Leave" if m.predict([val])[0]==1 else "Will Stay")

else:
    st.header("Employee Clustering")
    st.write("Cluster employees using KMeans model.")
    m = load_model("cluster_model.pkl")
    feats = st.multiselect("Select features", df.select_dtypes(include=[np.number]).columns.tolist(),
                           default=["Age","MonthlyIncome","DistanceFromHome"])
    if st.button("Run Clustering"):
        df["Cluster"] = m.predict(df[feats])
        st.dataframe(df[feats + ["Cluster"]])
