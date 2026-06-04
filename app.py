
import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Indian Startups Analysis",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/Indian_Startups.csv")
    except FileNotFoundError:
        return None

df = load_data()

# -----------------------------
# Banner
# -----------------------------
try:
    st.image("assets/banner.png", use_container_width=True)
except:
    st.title("🚀 Indian Startups Analysis & Prediction System")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚀 Indian Startups")
st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project Modules**

    📊 Data Overview

    📈 Visualizations

    🤖 Prediction

    💡 Insights
    """
)

st.sidebar.markdown("---")
st.sidebar.success("Use the pages menu above to navigate.")

# -----------------------------
# Main Title
# -----------------------------
st.title("🚀 Indian Startups Analysis & Prediction System")

st.markdown("""
Welcome to the **Indian Startups Dashboard**.

This application helps users analyze startup trends,
visualize funding patterns, and predict startup funding
using Machine Learning.
""")

# -----------------------------
# Dataset Metrics
# -----------------------------
if df is not None:

    st.subheader("📌 Quick Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Startups", len(df))

    with col2:
        st.metric("Industries", df["Industry"].nunique())

    with col3:
        st.metric("Cities", df["City"].nunique())

    with col4:
        st.metric(
            "Total Funding (Cr)",
            f"{df['Funding_Amount_Cr'].sum():,.0f}"
        )

# -----------------------------
# Project Features
# -----------------------------
st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Data Overview
    - View dataset
    - Check missing values
    - View statistics
    - Explore startup records
    """)

with col2:
    st.markdown("""
    ### 📈 Visualizations
    - Industry-wise analysis
    - City-wise analysis
    - Funding distribution
    - Startup trends
    """)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### 🤖 Prediction
    - Predict funding amount
    - Machine Learning model
    - Instant results
    """)

with col4:
    st.markdown("""
    ### 💡 Insights
    - Top funded startups
    - Startup hubs
    - Industry insights
    - Business conclusions
    """)

# -----------------------------
# Dataset Preview
# -----------------------------
if df is not None:

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

else:
    st.error(
        "Dataset not found! Please place "
        "'Indian_Startups.csv' inside the data folder."
    )

# -----------------------------
# About Project
# -----------------------------
st.subheader("📚 About the Project")

st.write("""
The Indian startup ecosystem has become one of the largest
and fastest-growing startup ecosystems in the world.

This project provides:

- Startup data analysis
- Funding trend visualization
- Industry comparison
- City-wise startup distribution
- Funding prediction using Machine Learning
- Business insights and conclusions

Technologies Used:
- Streamlit
- Pandas
- Plotly
- Scikit-Learn
- Joblib
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
    "<center><h4>🚀 Indian Startups Analysis & Prediction System</h4></center>",
    unsafe_allow_html=True
)

st.markdown(
    "<center>Developed using Streamlit, Machine Learning and Data Analytics</center>",
    unsafe_allow_html=True
)
