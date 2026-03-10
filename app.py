import streamlit as st
import pandas as pd
from monday_client import fetch_deals, fetch_work_orders
from llm_agent import generate_insight

st.set_page_config(page_title="Monday BI Agent", layout="wide")

st.title("Monday.com Business Intelligence Agent")

st.write("Fetching data from monday.com...")

# Fetch data
try:
    deals_df = fetch_deals()
    work_orders_df = fetch_work_orders()
except Exception as e:
    st.error(f"Error fetching data from monday.com: {e}")
    st.stop()


# =========================
# DATA OVERVIEW
# =========================

st.header("Data Overview")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Deals Data")
    st.dataframe(deals_df)

with col2:
    st.subheader("Work Orders Data")
    st.dataframe(work_orders_df)


# =========================
# BASIC BUSINESS METRICS
# =========================

st.header("Business Metrics")

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

try:
    deals_df["Masked Deal value"] = pd.to_numeric(
        deals_df["Masked Deal value"], errors="coerce"
    )
    total_pipeline = deals_df["Masked Deal value"].sum()
except:
    total_pipeline = 0

with metrics_col1:
    st.metric("Total Pipeline Value", f"${total_pipeline:,.0f}")

with metrics_col2:
    st.metric("Total Deals", len(deals_df))

with metrics_col3:
    st.metric("Total Work Orders", len(work_orders_df))


# =========================
# DEAL STATUS ANALYSIS
# =========================

if "Deal Status" in deals_df.columns:
    st.header("Deal Status Distribution")

    status_counts = deals_df["Deal Status"].value_counts()

    st.bar_chart(status_counts)


# =========================
# DATA QUALITY CHECKS
# =========================

st.header("Data Quality Checks")

issues = []

if "Masked Deal value" in deals_df.columns:
    missing_values = deals_df["Masked Deal value"].isna().sum()
    if missing_values > 0:
        issues.append(f"{missing_values} deals have missing deal values")

if "Close Date (A)" in deals_df.columns:
    missing_dates = deals_df["Close Date (A)"].isna().sum()
    if missing_dates > 0:
        issues.append(f"{missing_dates} deals missing close dates")

if len(issues) == 0:
    st.success("No major data quality issues detected")
else:
    for issue in issues:
        st.warning(issue)


# =========================
# FOUNDER QUESTION INTERFACE
# =========================

st.header("Ask a Business Question")

question = st.text_input(
    "Example: How is our pipeline looking for high probability deals?"
)

if question:

    context = f"""
Total Pipeline Value: {total_pipeline}
Total Deals: {len(deals_df)}
Total Work Orders: {len(work_orders_df)}

Deal Status Distribution:
{deals_df['Deal Status'].value_counts() if 'Deal Status' in deals_df.columns else 'Unknown'}
"""

    response = generate_insight(question, context)

    st.subheader("Agent Response")
    st.write(response)
# =========================
# LEADERSHIP SUMMARY
# =========================

st.header("Generate Leadership Update")

if st.button("Generate Leadership Summary"):

    st.subheader("Leadership Update")

    st.write(f"Pipeline Value: ${total_pipeline:,.0f}")
    st.write(f"Total Deals: {len(deals_df)}")
    st.write(f"Total Work Orders: {len(work_orders_df)}")

    if "Deal Status" in deals_df.columns:
        status_counts = deals_df["Deal Status"].value_counts()

        st.write("Deal Status Breakdown:")
        st.write(status_counts)