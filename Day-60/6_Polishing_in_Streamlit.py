"""
📌 Streamlit - Step 6 (Polish & Portfolio)

Today we will polish our Streamlit app so it looks professional and is portfolio-ready.
We’ll learn:
    1. How to create a custom theme (config.toml)
    2. How to style with HTML/CSS in Streamlit
    3. How to add logos and icons
    4. How to organize a multi-page app
By the end of this, we’ll have a polished, reusable structure.

This file covers:
    - Custom theme via config.toml
    - HTML/CSS styling
    - Adding logos and icons
    - Multi-page navigation
    - Portfolio-ready app setup

📝 Summary:
    - config.toml → theme customization
    - st.markdown() → HTML/CSS styling
    - st.image() → add logos/icons
    - Multi-page navigation → structure app

"""

import streamlit as st
import os

# =====================================================
# ============ PAGE CONFIGURATION ===================
# =====================================================

# st.set_page_config() allows us to set:
#     - page title
#     - favicon
#     - layout (wide or centered)
#     - initial sidebar state
#
# This helps make our app look professional from the start.

st.set_page_config(
    page_title="Portfolio App",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# ============ CUSTOM THEME SETUP ====================
# =====================================================

# To create a custom theme, we use a file named config.toml
# This should be placed in the root directory of our project.
#
# Example config.toml content:
# ----------------------------------------------------
# [theme]
# primaryColor = "#4CAF50"
# backgroundColor = "#f0f2f6"
# secondaryBackgroundColor = "#e0e0e0"
# textColor = "#333333"
# font = "sans serif"
# ----------------------------------------------------
#
# This theme will apply globally to our app.

st.markdown("### 🎨 Custom theme is applied via config.toml")

# =====================================================
# ============ HTML & CSS STYLING ====================
# =====================================================

# We can style text, headers, background and layout using HTML and CSS inside st.markdown().
# unsafe_allow_html=True must be set to allow HTML/CSS.

st.markdown(
    """
    <style>
    h1 {
        color: #4CAF50;
        font-size: 40px;
        text-align: center;
    }
    h2 {
        color: #333333;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .custom-text {
        color:#555;
        font-style:italic;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='big-font'>Welcome to Our Portfolio App 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p class='custom-text'>We are making our app look polished and professional using custom styling.</p>",
            unsafe_allow_html=True)

# =====================================================
# ============ ADDING LOGO AND ICONS =================
# =====================================================

# Adding logos and icons gives your app branding and professionalism.
# We can use st.image() to add images to our app.

logo_path = os.path.join("assets", "logo.png")  # Place logo in assets folder
if os.path.exists(logo_path):
    st.image(logo_path, width=150, caption="Our Brand Logo")
else:
    st.warning("Logo not found in assets/logo.png")

st.markdown("### :sparkles: Adding a personalized branding touch")

# =====================================================
# ============ MULTI-PAGE NAVIGATION =================
# =====================================================

# A multi-page app makes your project more organized.
# We use st.sidebar.radio() to create navigation.

st.header("Multi-Page Navigation Example")

page = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Dashboard", "About"],
    help="Use sidebar to switch between pages"
)

if page == "Home":
    st.subheader("🏠 Home Page")
    st.write("Welcome to the home page of our polished portfolio app.")
    st.markdown("<p class='custom-text'>Here we can add an introduction and highlights.</p>", unsafe_allow_html=True)

elif page == "Dashboard":
    st.subheader("📊 Dashboard")
    st.write("This page contains the main functionality and data visualizations.")
    st.markdown("<p class='custom-text'>This can include charts, tables, and reports.</p>", unsafe_allow_html=True)

elif page == "About":
    st.subheader("ℹ️ About Page")
    st.write("This page contains information about the project and developer.")
    st.markdown("<p class='custom-text'>We can add contact info, portfolio links, and acknowledgements.</p>",
                unsafe_allow_html=True)

# =====================================================
# ================= QUICK RECAP ======================
# =====================================================
"""
Quick Recap:
- config.toml → allows us to set global app theme colors, fonts, and backgrounds.
- st.markdown() → we can use HTML/CSS to customize the look of our app.
- st.image() → add logos and icons to give branding.
- Multi-page navigation → structure app for better UX.
- Portfolio-ready app → clean, professional, and easy to share.
"""
