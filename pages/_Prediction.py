import streamlit as st
import pandas as pd
import joblib

# Page Title
st.title("🤖 Startup Funding Prediction")

# Load Model
@st.cache_resource
def load_model():
    return joblib.load("models/Indian_Startups.pkl")

model = load_model()

st.subheader("Enter Startup Details")

# User Inputs
founded_year = st.number_input(
    "Founded Year",
    min_value=2000,
    max_value=2030,
    value=2018
)

employees = st.number_input(
    "Number of Employees",
    min_value=1,
    value=100
)

# Prediction Button
if st.button("Predict Funding Amount"):
    
    # Create Input DataFrame
    input_data = pd.DataFrame({
        "Founded_Year": [founded_year],
        "Employees": [employees]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Funding Amount: ₹ {prediction:.2f} Crores"
    )
