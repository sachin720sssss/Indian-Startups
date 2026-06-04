import streamlit as st
import pandas as pd
import plotly.express as px

# Page Title
st.title("📈 Startup Visualizations")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/Indian_Startups.csv")

df = load_data()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Industry Distribution
st.subheader("🏢 Industry-wise Startup Count")

industry_count = df["Industry"].value_counts().reset_index()
industry_count.columns = ["Industry", "Count"]

fig1 = px.bar(
    industry_count,
    x="Industry",
    y="Count",
    title="Industry-wise Startup Count"
)

st.plotly_chart(fig1, use_container_width=True)

# City Distribution
st.subheader("🌆 City-wise Startup Count")

city_count = df["City"].value_counts().reset_index()
city_count.columns = ["City", "Count"]

fig2 = px.pie(
    city_count,
    names="City",
    values="Count",
    title="City-wise Startup Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Funding by Industry
st.subheader("💰 Funding Amount by Industry")

industry_funding = (
    df.groupby("Industry")["Funding_Amount_Cr"]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    industry_funding,
    x="Industry",
    y="Funding_Amount_Cr",
    title="Total Funding by Industry"
)

st.plotly_chart(fig3, use_container_width=True)

# Funding Stage Distribution
st.subheader("🚀 Funding Stage Distribution")

stage_count = df["Funding_Stage"].value_counts().reset_index()
stage_count.columns = ["Stage", "Count"]

fig4 = px.pie(
    stage_count,
    names="Stage",
    values="Count",
    title="Funding Stage Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# Employees vs Funding
st.subheader("👨‍💼 Employees vs Funding")

fig5 = px.scatter(
    df,
    x="Employees",
    y="Funding_Amount_Cr",
    color="Industry",
    hover_name="Startup_Name",
    title="Employees vs Funding Amount"
)

st.plotly_chart(fig5, use_container_width=True)

# Founded Year Distribution
st.subheader("📅 Startup Founded Year Distribution")

fig6 = px.histogram(
    df,
    x="Founded_Year",
    nbins=10,
    title="Founded Year Distribution"
)

st.plotly_chart(fig6, use_container_width=True)
