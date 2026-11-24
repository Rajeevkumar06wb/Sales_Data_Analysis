
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Dashboard page settings
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Dataset path
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "Dataset" / "Superstore_Cleaned.csv"

# Load dataset
df = pd.read_csv(file_path, parse_dates=["Order Date"])

# Dashboard heading
st.title("📊 Sales Data Analysis Dashboard")
st.write("Interactive Sales Performance Dashboard")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Apply filters
filtered_df = df.copy()

# Date Range Filter
st.sidebar.subheader("Select Date Range")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Choose Start and End Date",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date) &
        (filtered_df["Order Date"].dt.date <= end_date)
    ]


if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# Calculate business metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_customers = filtered_df["Customer ID"].nunique()

# Display KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Total Customers", f"{total_customers:,}")

st.divider()

# Category-wise sales chart
st.subheader("Sales by Category")

category_sales = filtered_df.groupby("Category", as_index=False)["Sales"].sum()

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# Region-wise profit chart
st.subheader("Profit by Region")

region_profit = filtered_df.groupby("Region", as_index=False)["Profit"].sum()

fig2 = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    color="Region",
    title="Region-wise Profit"
)

st.plotly_chart(fig2, use_container_width=True)

# Region-wise Sales Pie Chart
st.subheader("Region-wise Sales Distribution")

region_sales = (
    filtered_df.groupby("Region", as_index=False)["Sales"].sum()
)

fig4 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales Distribution by Region",
    hole=0.4
)

st.plotly_chart(fig4, use_container_width=True)


# Monthly sales trend
st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby(
        pd.Grouper(key="Order Date", freq="MS")
    )["Sales"].sum().reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# Top 10 products
st.subheader("Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .nlargest(10)
    .reset_index()
)

st.dataframe(top_products, use_container_width=True)

# Complete dataset
with st.expander("View Complete Sales Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# Download Filtered Sales Data
st.subheader("Download Sales Report")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sales Report (CSV)",
    data=csv_data,
    file_name="Sales_Report.csv",
    mime="text/csv"
)

st.success("Dashboard Loaded Successfully!")
