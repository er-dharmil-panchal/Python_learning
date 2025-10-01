"""
📌 Streamlit - Step 1 (Foundations of Streamlit)
    - Streamlit is a Python library that lets you create interactive web apps easily.
    - Instead of learning HTML, CSS, JavaScript, you just use Python code to build apps.
    - You run streamlit run app.py → instantly you get a web app in your browser.

   This file covers:
    - Installing & Running Streamlit
    - Text & Display Elements
    - Tables & Dataframes
    - Quick Charts
    - External Plots (Matplotlib/Seaborn)

📝 Summary:
    - st.text() → only plain text
    - st.write() → smart display (text, numbers, dataframes, charts…)
    - st.table() → static tables
    - st.dataframe() → interactive tables
    - Quick charts (line, bar, scatter) → shortcuts
    - External plots → use st.pyplot()


# =====================================================
# ================== Introduction =====================
# =====================================================

⦿ What is Streamlit?
    - Streamlit is a Python library that lets you create interactive web apps easily.
    - Instead of learning HTML, CSS, JavaScript, you just use Python code to build apps.
    - You run streamlit run app.py → instantly you get a web app in your browser.

⦿ Why Streamlit?
    - Simplicity → You write Python, it turns into a UI.
    - Data-first → Built for data scientists & ML engineers.
    - Fast Prototyping → In minutes, you can create a working app.
    - Deployment-ready → Easy to share dashboards and ML models with non-programmers.

⦿ Where Streamlit is Used in Industry?
    - Dashboards → Financial analytics, marketing dashboards, sales monitoring.
    - ML Demos → Share a trained model with business teams for testing.
    - Data Exploration Tools → Upload CSV/Excel, explore interactively.
    - Prototyping → Quickly test an idea before investing in big web frameworks.

🔥 In short → Streamlit = Fast way to make Python projects usable by others.
"""
# 📌
# =====================================================
# ============ Install & Run Streamlit ================
# =====================================================

# Install -> pip install streamlit
# Run this command -> streamlit hello
# A demo app will open in your browser

# 👉🏻 Creating first page.
import streamlit as st
import pandas as pd

st.title("This is my first page using Streamlit and this is title ✨")
# To run this we have to do -> streamlit run filename


# 📌
# =====================================================
# ============ Text & Display Elements ================
# =====================================================

st.title("Streamlit Basics")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("Plain Text")
st.markdown(
    "**Bold Text**, *Italic Text*, and [Links - Click me 😉](https://www.linkedin.com/in/dharmil-panchal-999501332/)")
st.write("Smart display: numbers, dataframes, text, almost anything!")
# write can show text, number, dataframe and all but st.text will accept only plain text

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.subheader("st.write() print dataframe like table same as st.dataframe()")
# st.dataframe(df)
st.write(df)  # nice interactive table
st.subheader("st.text() convert dataframe in plain text")
st.text(df)  # plain text output of DataFrame

# 📌
# =====================================================
# ============== Tables & Dataframes ==================
# =====================================================

st.title("Tables & Dataframes")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)

st.subheader("st.table() print static table")
st.table(df)  # static table

st.subheader("st.dataframe() print interactive table")
st.dataframe(df)  # interactive table
st.text("👉 Difference: st.table = fixed, st.dataframe = scrollable, sortable, can download, search")

# 📌
# =====================================================
# =================== Quick Charts ====================
# =====================================================

st.title("Quick Charts")
st.subheader("Can convert in table also")
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
st.scatter_chart(chart_data)

st.text("👉 These are shortcuts for quick visualizations.")

# 📌
# =====================================================
# ======= External Plots (Matplotlib/Seaborn) =========
# =====================================================

st.title("External Plots (Matplotlib/Seaborn)")
import matplotlib.pyplot as plt
import seaborn as sns

# Sample plot
fig, ax = plt.subplots()
sns.histplot(df["Age"], bins=5)
st.pyplot(fig)

df = sns.load_dataset("tips")
pairplot_fig = sns.pairplot(df, hue="sex")
st.pyplot(pairplot_fig.fig)  # Show pairplot figure
st.text("👉 Can plot by st.pyplot()")

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- st.text() → only plain text
- st.write() → flexible, can show numbers, text, dataframe, plots
- st.table() → static table
- st.dataframe() → interactive table
- Quick Charts → line_chart, bar_chart, scatter_chart
- External plots (Matplotlib/Seaborn) → st.pyplot(fig)
"""