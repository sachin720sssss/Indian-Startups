import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Indian Startups Analysis",
    page_icon="🚀",
    layout="wide"
)

# Banner
try:
    st.image("assets/banner.png", use_container_width=True)
except:
    pass

# Title
st.title("🚀 Indian Startups Analysis & Prediction System")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info(
    """
    Use the pages in the sidebar to explore:
    
    📊 Data Overview  
    📈 Visualizations  
    🤖 Prediction  
    💡 Insights
    """
)

# Home Page Content
st.header("Welcome to Indian Startups Dashboard")

st.write("""
This project provides analysis and prediction based on Indian startup data.

### Features:
- Data Overview
- Interactive Visualizations
- Startup Prediction
- Business Insights
""")

# Metrics Section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Startups Analyzed", "500+")

with col2:
    st.metric("Industries", "20+")

with col3:
    st.metric("Cities", "50+")

# About Dataset
st.subheader("About the Dataset")

st.write("""
The dataset contains information about Indian startups such as:

- Startup Name
- Industry
- City
- Funding Amount
- Investors
- Year Founded
- Funding Stage

Use the navigation menu on the left to explore the data.
""")

# Footer
st.markdown("---")
st.markdown("Developed using Streamlit, Pandas, Plotly and Scikit-Learn.")
