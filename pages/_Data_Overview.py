import streamlit as st
import pandas as pd

# Page Title
st.title("📊 Data Overview")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/Indian_Startups.csv")

df = load_data()

# Display Dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Dataset Shape
st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

# Column Information
st.subheader("Column Names")
st.write(list(df.columns))

# Data Types
st.subheader("Data Types")
st.dataframe(df.dtypes.astype(str).reset_index().rename(
    columns={"index": "Column", 0: "Data Type"}
))

# Missing Values
st.subheader("Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]
st.dataframe(missing)

# Statistical Summary
st.subheader("Statistical Summary")
st.dataframe(df.describe())

# Industry Distribution
st.subheader("Industry Distribution")
st.dataframe(df["Industry"].value_counts())

# City Distribution
st.subheader("City Distribution")
st.dataframe(df["City"].value_counts())

# Dataset Download
st.subheader("Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="Indian_Startups.csv",
    mime="text/csv"
)
