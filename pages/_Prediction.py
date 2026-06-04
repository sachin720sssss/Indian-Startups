import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Funding Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Startup Funding Prediction")
st.markdown("Predict the estimated funding amount for a startup based on its details.")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    model_path = "models/Indian_Startups.pkl"

    if not os.path.exists(model_path):
        return None

    return joblib.load(model_path)

model = load_model()

# -----------------------------
# Check Model Availability
# -----------------------------
if model is None:
    st.error(
        "Model file not found!\n\n"
        "Please place 'Indian_Startups.pkl' inside the models folder."
    )
    st.stop()

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("📋 Enter Startup Details")

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
# Prediction Button
# -----------------------------
if st.button("🔮 Predict Funding"):

    try:
        # Create DataFrame
        input_data = pd.DataFrame({
            "Founded_Year": [founded_year],
            "Employees": [employees]
        })

        # Predict
        prediction = model.predict(input_data)[0]

        st.success(
            f"Estimated Funding Amount: ₹ {prediction:.2f} Crores"
        )

        # Funding Category
        if prediction < 500:
            category = "🌱 Early Stage Startup"
        elif prediction < 1000:
            category = "🚀 Growth Stage Startup"
        else:
            category = "🏆 Highly Funded Startup"

        st.info(f"Category: {category}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# -----------------------------
# Sample Inputs
# -----------------------------
st.markdown("---")
st.subheader("📝 Example Values")

sample_df = pd.DataFrame({
    "Founded_Year": [2015, 2018, 2021],
    "Employees": [500, 1500, 3000]
})

st.dataframe(sample_df, use_container_width=True)

# -----------------------------
# About Model
# -----------------------------
st.markdown("---")
st.subheader("ℹ About the Model")

st.write("""
This prediction model uses a **Random Forest Regressor**
trained on the startup dataset.

### Features Used:
- Founded Year
- Number of Employees

### Prediction Target:
- Funding Amount (in Crores)

The prediction is an estimate based on patterns learned
from the training data.
""")
