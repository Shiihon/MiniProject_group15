import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# Page configuration
st.set_page_config(page_title="Wine Quality Visualizer", layout="wide")
st.title("🍷 Wine Quality Visualizer")

# Introduction
st.markdown("""
This application provides an interactive exploratory analysis of physicochemical properties and quality scores of wines.  
The dataset includes measurements for red and white **Vinho Verde** wines. Each sample is characterized by multiple variables  
(e.g., acidity, sugar, pH, alcohol) along with a **quality rating** (0–10) assigned by sensory evaluation.

You can explore:
- **Red**, **White**, or **Combined** wine datasets
- Descriptive statistics for all numeric features
- Interactive **2D**, **3D**, and other visualization tools to uncover trends, correlations, and groupings
""")

# Sidebar: Dataset selection
st.sidebar.header("Dataset Selection")
dataset_option = st.sidebar.selectbox(
    "Choose a wine dataset:",
    ["Red Wine", "White Wine", "Both Combined"]
)

# Load CSV with delimiter detection
@st.cache_data
def load_data(file_path, wine_type=None):
    with open(file_path, 'r') as f:
        sample = f.read(2048)
        dialect = csv.Sniffer().sniff(sample)
        f.seek(0)
        df = pd.read_csv(f, delimiter=dialect.delimiter)
    
    if wine_type:
        df["wine_type"] = wine_type

    return df

# Load based on selection (paths relative to /app/)
if dataset_option == "Red Wine":
    df = load_data("../red_wine_cleaned.csv", wine_type="Red")
elif dataset_option == "White Wine":
    df = load_data("../white_wine_cleaned.csv", wine_type="White")
else:
    df = load_data("../red_white_wine_cleaned.csv")  # Already includes 'wine_type'

# Preview of dataset
st.subheader("📄 Dataset Preview")
st.markdown("The table below shows a sample of the dataset containing chemical properties and the quality score of each wine sample.")
st.write(df.head())

# Descriptive statistics
st.subheader("📊 Descriptive Statistics")
st.markdown("This table summarizes the central tendency and spread of each numeric variable in the dataset.")
st.write(df.describe())

# List of numeric columns
numeric_columns = df.select_dtypes(include='number').columns.tolist()

# Stop app if no numeric data
if not numeric_columns:
    st.error("No numeric columns found in the dataset.")
    st.stop()

# 2D Scatter Plot
st.subheader("📈 2D Scatter Plot")
st.markdown("""
Choose any two numerical variables to visualize their pairwise relationship.
Use the color dropdown to segment data by wine type or other numeric attributes such as alcohol or quality.
""")
col1, col2 = st.columns(2)
with col1:
    x2d = st.selectbox("X-axis", numeric_columns, key="2d_x")
with col2:
    y2d = st.selectbox("Y-axis", numeric_columns, key="2d_y")

color2d = st.selectbox("Color by", [None, "wine_type"] + numeric_columns, key="2d_color")
fig2d = px.scatter(df, x=x2d, y=y2d, color=color2d,
                   title=f"2D Scatter Plot: {x2d} vs {y2d}")
st.plotly_chart(fig2d, use_container_width=True)

# 3D Scatter Plot
st.subheader("🧊 3D Scatter Plot")
st.markdown("""
Visualize three numeric variables simultaneously in a 3D space.  
This is helpful for detecting groupings, clusters, or interactions between features that may not be apparent in 2D.
""")
col3, col4, col5 = st.columns(3)
with col3:
    x3d = st.selectbox("X-axis", numeric_columns, key="3d_x")
with col4:
    y3d = st.selectbox("Y-axis", numeric_columns, key="3d_y")
with col5:
    z3d = st.selectbox("Z-axis", numeric_columns, key="3d_z")

color3d = st.selectbox("Color by", [None, "wine_type"] + numeric_columns, key="3d_color")
fig3d = px.scatter_3d(df, x=x3d, y=y3d, z=z3d, color=color3d,
                      title=f"3D Scatter Plot: {x3d}, {y3d}, {z3d}")
st.plotly_chart(fig3d, use_container_width=True)

# Correlation Heatmap
st.subheader("🧮 Correlation Heatmap")
st.markdown("""
This heatmap shows the correlation coefficients between numerical features in the dataset.  
It helps identify variables with strong linear relationships that may influence wine quality.
""")
fig_corr, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df[numeric_columns].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig_corr)

# Histogram of selected feature
st.subheader("📉 Histogram")
st.markdown("""
Displays the distribution of a selected numerical feature.  
Histogram bins reveal the shape, skew, and spread of the data across samples.
""")
selected_feature = st.selectbox("Select feature for histogram", numeric_columns)
fig_hist = px.histogram(df, x=selected_feature,
                        color="wine_type" if "wine_type" in df.columns else None,
                        nbins=30,
                        title=f"Distribution of {selected_feature}")
st.plotly_chart(fig_hist, use_container_width=True)

# Box Plot for feature by wine type or quality
st.subheader("📦 Box Plot")
st.markdown("""
Box plots provide a compact view of the distribution of a feature across different groups,  
highlighting median, interquartile range, and potential outliers.
""")
y_feature = st.selectbox("Feature to analyze", numeric_columns, key="boxplot_feature")
group_by = st.selectbox("Group by", ["wine_type", "quality"] if "wine_type" in df.columns else ["quality"])

fig_box = px.box(df, x=group_by, y=y_feature, color=group_by,
                 title=f"Box Plot of {y_feature} grouped by {group_by}")
st.plotly_chart(fig_box, use_container_width=True)