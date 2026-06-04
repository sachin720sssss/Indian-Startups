import streamlit as st
import pandas as pd

# Page Title
st.title("💡 Startup Insights")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/Indian_Startups.csv")

df = load_data()

# Total Startups
st.subheader("📊 Overall Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Startups", len(df))

with col2:
    st.metric("Total Industries", df["Industry"].nunique())

with col3:
    st.metric("Total Cities", df["City"].nunique())

# Top Funded Startup
st.subheader("🏆 Top Funded Startup")

top_startup = df.loc[df["Funding_Amount_Cr"].idxmax()]

st.success(
    f"{top_startup['Startup_Name']} received "
    f"₹{top_startup['Funding_Amount_Cr']} Cr funding."
)

# Top Industry
st.subheader("🏢 Most Popular Industry")

top_industry = df["Industry"].value_counts().idxmax()

st.info(f"Most startups belong to the **{top_industry}** industry.")

# Top City
st.subheader("🌆 Startup Hub")

top_city = df["City"].value_counts().idxmax()

st.info(f"**{top_city}** has the highest number of startups.")

# Average Funding
st.subheader("💰 Average Funding")

avg_funding = df["Funding_Amount_Cr"].mean()

st.success(f"Average Funding Amount: ₹{avg_funding:.2f} Cr")

# Industry-wise Funding
st.subheader("📈 Industry-wise Funding")

industry_funding = (
    df.groupby("Industry")["Funding_Amount_Cr"]
    .sum()
    .sort_values(ascending=False)
)

st.dataframe(industry_funding)

# Funding Stage Insights
st.subheader("🚀 Funding Stage Analysis")

stage_counts = df["Funding_Stage"].value_counts()

st.dataframe(stage_counts)

# Key Insights
st.subheader("🔍 Key Business Insights")

st.markdown("""
### Important Findings

- Bengaluru is a major startup hub.
- FinTech and E-Commerce dominate the startup ecosystem.
- Growth-stage startups attract significant funding.
- Startups with more employees generally receive higher funding.
- Recently founded startups are gaining investor interest.
""")

# Conclusion
st.subheader("📌 Conclusion")

st.write("""
The Indian startup ecosystem is growing rapidly, especially in
FinTech, E-Commerce, EdTech, and HealthTech sectors.
Cities such as Bengaluru, Mumbai, and Gurugram continue to
attract major investments and entrepreneurial activity.
""")
