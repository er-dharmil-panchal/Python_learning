"""
📌 Streamlit - Step 3 (State and Multiple Pages in Streamlit)
    - click a button, enter a value → but on the next rerun, it disappears,
        Solution -
            - st.session_state → like app memory.
            - This allows counters, login info, or filters to persist across user interactions.
    - Streamlit has a pages/ folder system → each file becomes a new page in the sidebar.
        - Users can switch between pages just like a real website.
    - Instead of a long scroll, we can organize our app into columns, tabs, expanders.
        - This makes dashboards look professional and user-friendly.

     This file covers:
    - State Management with st.session_state
    - Linking Widgets with Session State
    - on_change Callbacks
    - Manual Sidebar Navigation for Multiple Pages
    - Pages Folder System Overview
    - Layouts with Columns and Expanders
    - Media Embedding (Images, Audio, Video)
    - Download Buttons

📝 Summary:
    - State Management → persistent variables and widget values.
    - Multiple Pages → better organization and navigation.
    - Layouts → cleaner design.
    - Media → richer user experience.
    - Download → exporting processed data.
"""
import streamlit as st
import pandas as pd

st.title("Step 3 (State and Multiple Pages in Streamlit)")
# 📌
# =====================================================
# ================= State Management ==================
# =====================================================

# Problem - Streamlit re-runs the entire script every time a widget changes.
# you enter your name in a text box, and then click a button → the script reloads → input disappears.

# Solution -    Streamlit gives us st.session_state,
#               which acts like a dictionary to store values persistently across reruns.

st.header(" - Session State")

# Accessing / setting session state
st.subheader(" without state ")
dp = 0
st.write("Before:", dp)
# Button to increase count
if st.button("Increment"):
    # st.session_state.count += 1
    dp = dp + 1

# Button to reset
if st.button("Reset"):
    # st.session_state.count = 0
    pass
st.write("After:", dp)

st.subheader("With State")
if "x" not in st.session_state:
    st.session_state.x = 0  # initialize state variable

# Button to increase count
if st.button("Increment1"):
    st.session_state.x += 1

# Button to reset
if st.button("Reset1"):
    st.session_state.x = 0
st.write("Current Count:", st.session_state.x)

# Here "x" is just variable name it can be anything
# if "count" then st.session_state.count will show the count of click

# Linking Widgets with Session State
st.subheader("Linking Widgets with Session State")
st.write("All widgets can be linked with key → this key becomes the variable name in st.session_state.")

st.text_input("Enter your name", key="username")
# name = st.text_input("Enter your name",key="username")
if st.button("Greet"):
    st.write(f"Hello, {st.session_state.username} welcome on this website.")
    # st.write(f"Hello, {name} welcome on this website.")
# Callback function

st.subheader("on_change Callback with Widgets")
st.write("Instead of using buttons, you can trigger a function automatically when a widget changes.")


# Callback function
def update_age():
    st.session_state.updated_value = f"Age updated: {st.session_state.age}"


# Slider with on_change
st.slider("Enter your age", 0, 100, value=(20), step=1, key="age", on_change=update_age)

# Placeholder
placeholder = st.empty()

# Display result in placeholder
if "updated_value" in st.session_state:
    placeholder.write(st.session_state.updated_value)

st.subheader("Viewing Session State")
st.write("Session State:", st.session_state)

# 📌
# =====================================================
# ================== Multiple Pages ===================
# =====================================================

st.header("Multiple Pages")

# Streamlit makes this possible in two ways:
#   1. Using a pages/ folder → each Python file is automatically a page in the sidebar.
#   2. Using manual sidebar navigation with radio/selectbox → single file, multiple "views".

st.subheader("Manual sidebar approach")
st.write("Everything stays in one file.")
st.write("You can keep filters or widgets persistent across pages using st.session_state.")

st.sidebar.title("This is using Manual way")

page = st.sidebar.radio("Go to:", ["Home", "Data Explorer", "About"])

if "filters" not in st.session_state:
    st.session_state.filters = {}

st.sidebar.header("Filters")
age_filter = st.sidebar.slider("Age Filter", 0, 100, (50))
st.session_state.filters["age"] = age_filter

if page == "Home":
    st.header("🏠 Home Page")
    st.write("Welcome to the Multi-Page Streamlit App!")
    st.write("Age", st.session_state.filters["age"])

elif page == "Data Explorer":
    st.header("📊 Data Explorer Page")
    st.write("Age", st.session_state.filters["age"])
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df.head())

elif page == "About":
    st.header("ℹ️ About Page")
    st.write("This app is built with Streamlit for demonstration purposes.")
    st.write("Age", st.session_state.filters["age"])

# Pros:
#   - Keeps everything in one file
#   - Easier for small projects
#   - Great for step-by-step learning
# Cons:
#   - File gets large as app grows
#   - Code becomes harder to manage

st.subheader("Pages Folder System")
st.write("Using pages/ folder system")
st.write("Can see page1/2 option at top of sidebar")

# Pros:
#   - Cleaner code organization
#   - Automatic navigation menu
#   - Easier for large projects
# Cons:
#   - Slightly more setup initially
#   - Navigation logic is automatic (less control)

st.subheader("Example of st.tabs()")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Home", "Data", "About"])

with tab1:
    st.header("🏠 Home Tab")
    st.write("Welcome to the Home tab!")
    st.button("Click me in Home")

with tab2:
    st.header("📊 Data Tab")
    st.write("This tab can hold data exploration tools.")
    st.file_uploader("Upload CSV", type="csv")

with tab3:
    st.header("ℹ️ About Tab")
    st.write("This tab contains information about the app.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

# 🔥 Note: can pass session_state attribute in same file but not in pages/folder


# 📌
# =====================================================
# ============= Layouts, Media & Download =============
# =====================================================
# organizing layouts, adding media, and enabling downloads.

st.header("Layouts, Media & Download")

# Columns
st.subheader("Using Columns")
st.write("You can divide the page horizontally into multiple sections with st.columns().")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Button in Column 1")

with col2:
    st.checkbox("Checkbox in Column 2")

with col3:
    st.radio("Radio in Column 3", ["A", "B", "C"])

st.write("This allows for cleaner layouts and grouping of widgets.")

# Expanders
st.subheader("Using Expander")
st.write("Expanders hide content until clicked, useful for optional sections.")

with st.expander("See explanation"):
    st.write("""
        Expanders are useful to hide long explanations,
        FAQs, or extra data to keep the main UI clean.
    """)
    st.code("with st.expander('Details'):\n    st.write('Hidden content')")

# Media Embedding
st.subheader("Adding Media")
st.write("we can embed images, audio, and video easily.")

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo",
         width=200)

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# Download Button
st.subheader("Download Processed Data")
st.write("we can let users download data after processing.")

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv"
)

st.write("we now know how to organize layouts, embed media, and add download functionality.")

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- st.session_state → persistent app memory across reruns.
- Widgets can be linked with keys → accessible via st.session_state[key].
- on_change callbacks → trigger functions automatically when widget values change.
- Manual sidebar navigation → control multiple “pages” in one file.
- pages/ folder system → each file becomes a separate page in sidebar.
- st.columns() → horizontal layout division.
- st.expander() → hide/show optional content.
- st.image(), st.audio(), st.video() → embed media files.
- st.download_button() → let users download processed data.
"""
