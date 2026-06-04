import plotly.express as px
import pandas as pd


def industry_bar_chart(df):
    """
    Industry-wise startup count
    """
    industry_count = df["Industry"].value_counts().reset_index()
    industry_count.columns = ["Industry", "Count"]

    fig = px.bar(
        industry_count,
        x="Industry",
        y="Count",
        title="Industry-wise Startup Count"
    )

    return fig


def city_pie_chart(df):
    """
    City-wise startup distribution
    """
    city_count = df["City"].value_counts().reset_index()
    city_count.columns = ["City", "Count"]

    fig = px.pie(
        city_count,
        names="City",
        values="Count",
        title="City-wise Startup Distribution"
    )

    return fig


def funding_by_industry_chart(df):
    """
    Total funding by industry
    """
    funding = (
        df.groupby("Industry")["Funding_Amount_Cr"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        funding,
        x="Industry",
        y="Funding_Amount_Cr",
        title="Total Funding by Industry"
    )

    return fig


def employees_vs_funding_chart(df):
    """
    Employees vs funding scatter plot
    """
    fig = px.scatter(
        df,
        x="Employees",
        y="Funding_Amount_Cr",
        color="Industry",
        hover_name="Startup_Name",
        title="Employees vs Funding Amount"
    )

    return fig


def founded_year_histogram(df):
    """
    Startup founded year distribution
    """
    fig = px.histogram(
        df,
        x="Founded_Year",
        nbins=10,
        title="Founded Year Distribution"
    )

    return fig


def funding_stage_pie_chart(df):
    """
    Funding stage distribution
    """
    stage_count = df["Funding_Stage"].value_counts().reset_index()
    stage_count.columns = ["Funding Stage", "Count"]

    fig = px.pie(
        stage_count,
        names="Funding Stage",
        values="Count",
        title="Funding Stage Distribution"
    )

    return fig
