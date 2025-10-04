"""
📌 Streamlit - Step 4 (Metrics & Advanced Charts)
    - Step 1 covered quick charts and basic visualizations.
    - Step 4 focuses on advanced chart types, interactive metrics, and real-time dashboards.
    - Learn how to display KPIs, gauges, Plotly charts, Altair charts, and interactive layouts.

   This file covers:
    - st.metric() → display key numbers with delta values
    - Plotly charts → interactive, zoomable, hoverable
    - Altair charts → concise, declarative charts
    - Updating charts dynamically
    - Dashboard layout organization

📝 Summary:
    - st.metric() → for KPIs (Key Performance Indicators)
    - Plotly → powerful interactive visualizations
    - Altair → clean declarative charts
    - st.columns() → organize dashboard layouts
"""

# =====================================================
# ================== Metrics =========================
# =====================================================

import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Metrics & Advanced Charts in Streamlit")

st.header("KPIs with st.metric()")
col1, col2, col3 = st.columns(3)

col1.metric("Revenue", "$25,000", "+5%")
col2.metric("Orders", "1,200", "-3%")
col3.metric("Customer Satisfaction", "89%", "+2%")

st.text("👉 st.metric() is ideal for dashboards showing KPIs.")

# =====================================================
# ================== Plotly Charts ===================
# =====================================================

st.header("📈 Plotly Charts - Full Examples")

import plotly.express as px

# Sample Data
df = px.data.gapminder().query("year==2007")

# ---------------- Scatter Plot ----------------
st.subheader("Scatter Plot")
fig_scatter = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title="GDP vs Life Expectancy (2007)"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------- Line Chart ----------------
st.subheader("Line Chart")
df_line = px.data.gapminder().query("country=='India'")
fig_line = px.line(
    df_line,
    x="year",
    y="lifeExp",
    title="Life Expectancy Over Time in India"
)
st.plotly_chart(fig_line, use_container_width=True)

# ---------------- Bar Chart ----------------
st.subheader("Bar Chart")
df_bar = px.data.tips()
fig_bar = px.bar(
    df_bar,
    x="day",
    y="total_bill",
    color="sex",
    barmode="group",
    title="Total Bill by Day and Sex"
)
st.plotly_chart(fig_bar, use_container_width=True)

# ---------------- Area Chart ----------------
st.subheader("Area Chart")
fig_area = px.area(
    df_line,
    x="year",
    y="lifeExp",
    title="Area Chart - Life Expectancy Over Time"
)
st.plotly_chart(fig_area, use_container_width=True)

# ---------------- Pie Chart ----------------
st.subheader("Pie Chart")
fig_pie = px.pie(
    df,
    values="pop",
    names="continent",
    title="Population Distribution by Continent"
)
st.plotly_chart(fig_pie, use_container_width=True)

# ---------------- Histogram ----------------
st.subheader("Histogram")
fig_hist = px.histogram(
    df_bar,
    x="total_bill",
    nbins=20,
    title="Histogram of Total Bills"
)
st.plotly_chart(fig_hist, use_container_width=True)

# ---------------- Box Plot ----------------
st.subheader("Box Plot")
fig_box = px.box(
    df_bar,
    x="day",
    y="total_bill",
    color="sex",
    title="Box Plot - Total Bill by Day and Sex"
)
st.plotly_chart(fig_box, use_container_width=True)

# ---------------- Sunburst Chart ----------------
st.subheader("Sunburst Chart")
fig_sunburst = px.sunburst(
    df_bar,
    path=["day", "sex"],
    values="total_bill",
    title="Sunburst Chart - Bill Distribution"
)
st.plotly_chart(fig_sunburst, use_container_width=True)

st.text("✅ Plotly supports scatter, line, bar, area, pie, histogram, box, sunburst and many more charts.")


# =====================================================
# ================== Altair Charts ====================
# =====================================================

st.header("Altair Charts")

import altair as alt

source = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randn(10).cumsum()
})

chart = alt.Chart(source).mark_line(point=True).encode(
    x="x",
    y="y"
).interactive()

st.altair_chart(chart, use_container_width=True)
st.text("👉 Altair charts are concise and interactive.")

# =====================================================
# ================= Dynamic Chart Example =============
# =====================================================

st.header("Dynamic Chart Example")

n_points = st.slider("Select number of data points", 10, 100, 50)

dynamic_data = pd.DataFrame({
    "x": np.arange(n_points),
    "y": np.random.randn(n_points).cumsum()
})

st.line_chart(dynamic_data)

# =====================================================
# ================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- st.metric() → display key performance metrics.
- Plotly → interactive, zoomable charts with hover effects.
- Altair → declarative charts with minimal code.
- Dynamic charts → interactive data exploration.
- st.columns() → organize dashboard layout.
"""
