"""
📌 Streamlit - Step 2 (Widgets and Interactivity)
    - Streamlit Widgets make your app interactive.
    - Users can click buttons, select options, input text, upload files, and filter data.
    - We can react dynamically to user inputs and change outputs instantly.
    - Real power of Streamlit → creating interactive tools, not just static dashboards.

   This file covers:
    - Basic Input Widgets (Button, Checkbox, Radio, Selectbox, Slider, Text Input, Multiselect, Text Area)
    - Sidebar Navigation
    - File Uploads (CSV)
    - Forms
    - Mini Project: CSV Explorer

📝 Summary:
    - Widgets return values that can be used for conditional logic.
    - Sidebar → clean UI & navigation.
    - File Uploader → backbone of data explorer tools.
    - Forms → group inputs for better UX.
    - Mini Project → combining widgets to build a small interactive app.
"""

import streamlit as st
import pandas as pd

st.title("Step 2 - Widgets and Interactivity")
# 📌
# =====================================================
# ============== Basic Input Widgets ==================
# =====================================================

# Streamlit has ready-to-use input widgets. Each widget returns a value that you can use.

# Button
st.header("Button")
if st.button("Click this button", help="Click me 🙂"):
    st.text("Ohh! you really clicked. Thank you 🫡")
st.button(
    "Custom button",  # str
    key=None,  # str or int
    help="😎",  # str
    on_click=None,  # callable
    args=None,  # list/tuple
    kwargs=None,  # dict
    type="primary",  # "primary" | "secondary"
    disabled=False,  # bool
    use_container_width=False  # bool
)
# label (str, required) → text on the button.
# key (str/int, optional) → unique ID, lets you access button state in st.session_state.
# help (str, optional) → small tooltip when hovering.
# on_click (callable, optional) → function to execute immediately when button is clicked.
# args (list/tuple) → positional args for on_click.
# kwargs (dict) → keyword args for on_click.
# 👉🏻 type (str, default "secondary") → "primary" (blue highlight) vs "secondary" (default grey). Good for emphasizing main action.
# 👉🏻 disabled (bool, default False) → greys out the button, not clickable.
# use_container_width (bool, default False) → makes the button stretch full width of container/column.

# 👉🏻 on_click avoids writing if st.button(...): and keeps code cleaner for multiple buttons.
# 👉🏻 Multiple buttons in one page require unique keys if labels are the same.
st.subheader("Toggle button")
if st.toggle("toggle button"):
    st.text("on")

# Checkbox
st.header("Checkbox")
agree = st.checkbox("Agree", value=False)
dis_agree = st.checkbox("Disagree")
if agree:
    st.text("I also Agree")
if dis_agree:
    st.text("I also Disagree")
if agree and dis_agree:
    st.text("🤨Both ?")

st.subheader("Custom Checkbox")
st.checkbox(
    "Lable",  # str
    value=" ",  # bool
    key=None,  # str or int
    help="Hehe",  # str
    on_change=None,  # callable
    args=None,  # list/tuple
    kwargs=None,  # dict
    disabled=False,  # bool
    label_visibility="visible"  # "visible" | "hidden" | "collapsed"
)

# value (bool, default False) → initial state (checked/unchecked).
# disabled (bool) → greyed out, can’t be clicked.
# label_visibility (str, default "visible") →
#   "visible": normal label
#   "hidden": invisible but space reserved
#   "collapsed": label removed entirely (tight layout)


# Radio
st.header("Radio")
choice = st.radio("Pick one:", ["Option A", "Option B", "Option C"], index=None)
st.write("You selected:", choice)
# index = None will not select any radio button initially, (0 will pick 1st and so on)

st.subheader("Custom Radio Button")
st.radio(
    "Radio_Button!!",  # str
    [1, 2, 3, 4],  # list / tuple / np.array / pd.Series
    index=3,  # int or None
    key=None,  # str/int
    help="hehe",  # str
    on_change=None,  # callable
    args=None,  # list/tuple
    kwargs=None,  # dict
    disabled=False,  # bool
    horizontal=True,  # bool
    captions="ABCD",  # list of str
    # captions=['A','B','C','D'],           # list of str
    label_visibility="visible"  # "visible" | "hidden" | "collapsed"
)

# captions (list of str) → adds extra description under each option (like hints or icons). Length must match options.
# horizontal (bool, default False) →
#   False: vertical list (default).
#   True: inline horizontally (like tabs).

# 👉🏻 If captions length ≠ options length → error.

# Selectbox
st.header("Selectbox")
option = st.selectbox(
    "Choose a number",  # str
    [1, 2, 3, 4, 5],  # list / tuple / np.array / pd.Series
    index=None,  # int or None
    key=None,  # str/int
    help=None,  # str
    on_change=None,  # callable
    args=None,  # list/tuple
    kwargs=None,  # dict
    disabled=False,  # bool
    label_visibility="visible",  # "visible" | "hidden" | "collapsed"
    placeholder="🎈Select a number"  # str
)
st.write("Your choice:", option)

# Slider
st.subheader("Slider")
st.text("Singe sided - Slider (customized)")
value = st.slider("Select a range", min_value=0, max_value=100, value=(80), step=20, help="Hehe", format="%.2f",
                  label_visibility="visible")
st.write("Range selected:", value)
st.text("Double sided - Slider")
value = st.slider("Select a range", 0, 100, (10, 80))
st.write("Range selected:", value)

# format -> Formatting string for display (e.g., "%.2f" for 2 decimal places).
# step -> Increment between steps.
# value -> Default value. If tuple → range slider.

# 👉🏻 If step is not set → Streamlit chooses a step automatically based on range siz
# 👉🏻 For date/time sliders, step is not supported — use datetime.timedelta increments.
# Use label_visibility="collapsed" to hide label for clean UI.

# Text input
st.text("Text Area")
name = st.text_input("Enter your name")
if name:
    st.write("Hello,", name)

# =====================================================
# ================== Multiselect ======================
# =====================================================

st.header("Multiselect")
choices = st.multiselect(
    "Select multiple numbers",
    [1, 2, 3, 4, 5],
    default=[2, 4],
    help="Select one or more values"
)
st.write("You selected:", choices)

# Attributes:
# - options: list / tuple / np.array / pd.Series
# - default: list

# =====================================================
# ================== Text Area ========================
# =====================================================

st.header("Text Area")
feedback = st.text_area(
    "Enter your feedback",
    height=150,
    max_chars=500,
    placeholder="Type here...",
    help="Write something about your experience"
)
if feedback:
    st.write("Your feedback:", feedback)

# Attributes:
# - height: int
# - max_chars: int

# =====================================================
# ================ Sidebar Navigation =================
# =====================================================

st.header("Sidebar Navigation Example")
st.sidebar.title("Sidebar Filters")

page = st.sidebar.radio(
    "Go to:",
    ["Home", "Dashboard", "About"],
    help="Use sidebar to navigate between pages"
)
st.write("You are on the:", page, "page")

# can also do this. ( using with keyword )
# with st.sidebar:
#     st.title("Sidebar Example")
#     name = st.text_input("Enter your name")
#     age = st.slider("Select Age", 18, 60, 25)
#     choice = st.radio("Pick one:", ["Option A", "Option B", "Option C"])


# 👉 Use sidebar for navigation, filters, settings.

# =====================================================
# =================== File Uploads ====================
# =====================================================

st.header("Upload CSV Example")
file = st.file_uploader("Upload a CSV file", type="csv", help="Upload your CSV file for preview")

if file is not None:
    df = pd.read_csv(file)
    st.subheader("Data Preview:")
    st.dataframe(df.head())
    st.write("File uploaded successfully ✅")

# 👉 This is the backbone of your CSV Explorer project.


# =====================================================
# ======================= Forms =======================
# =====================================================

st.header("Forms Example")
with st.form("user_form", clear_on_submit=True):
    name = st.text_input("Enter Name", placeholder="Type your name")
    age = st.slider("Select Age", 18, 60, 25, help="Select your age")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Hello {name}, you are {age} years old.")

# 👉 Useful for login, registration, or data entry forms.


# =====================================================
# ============ Mini Project: CSV Explorer =============
# =====================================================

st.title("CSV Explorer App 🗂️")

# Upload CSV
file = st.file_uploader("Upload your CSV file", type="csv", help="Upload a CSV file to explore data")

if file is not None:
    df = pd.read_csv(file)
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Select columns
    cols = st.multiselect("Select columns to display", df.columns.tolist(), help="Choose columns to view")
    if cols:
        st.subheader("Filtered Data:")
        st.dataframe(df[cols])

    # Chart
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    chart_cols = st.multiselect(
        "Select numeric columns for chart",
        numeric_cols,
        help="Pick numeric columns to plot"
    )
    if chart_cols:
        st.subheader("Line Chart")
        st.line_chart(df[chart_cols])

# 👉 What this does:
# 1. Upload CSV
# 2. Preview table
# 3. Choose columns to display
# 4. Plot charts of numeric columns


# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- Button → trigger actions or run functions
- Checkbox → toggle True/False state
- Radio → single choice selection (vertical/horizontal)
- Selectbox → dropdown single choice selection with placeholder
- Slider → single or range numeric selection
- Text Input → single-line text input
- Multiselect → multiple choice selection
- Text Area → multi-line text input
- Sidebar → place widgets in a sidebar for navigation or filters
- File Uploader → upload CSV/Excel files for interactive display
- Form → group multiple inputs together with a submit button
- CSV Explorer → upload CSV, preview data, select columns, plot charts
"""
