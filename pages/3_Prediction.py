import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Funding Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Startup Funding Prediction")

# -----------------------------
# Load Data and Train Model
# -----------------------------
@st.cache_resource
def train_model():
    df = pd.read_csv("data/Indian_Startups.csv")

    X = df[["Founded_Year", "Employees"]]
    y = df["Funding_Amount_Cr"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model

model = train_model()

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Enter Startup Details")

col1, col2 = st.columns(2)

with col1:
    founded_year = st.number_input(
        "Founded Year",
        min_value=2000,
        max_value=2030,
        value=2018
    )

with col2:
    employees = st.number_input(
        "Number of Employees",
        min_value=1,
        max_value=100000,
        value=100
    )

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Funding Amount"):

    input_data = pd.DataFrame({
        "Founded_Year": [founded_year],
        "Employees": [employees]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Funding Amount: ₹ {prediction:.2f} Crores"
    )

    if prediction < 500:
        st.info("🌱 Early Stage Startup")
    elif prediction < 1000:
        st.info("🚀 Growth Stage Startup")
    else:
        st.info("🏆 Highly Funded Startup")

# -----------------------------
# About
# -----------------------------
st.markdown("---")
st.subheader("Model Information")

st.write("""
This page trains a Random Forest model directly from the
dataset and predicts the funding amount based on:

- Founded Year
- Number of Employees

No .pkl file is required.
""")
