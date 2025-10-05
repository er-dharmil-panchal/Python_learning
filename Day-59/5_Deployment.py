"""
📌 Streamlit - Step 5 (Deployment & Publishing)
   This file covers:
    - Exporting requirements.txt
    - Pushing project to GitHub
    - Deploying on Streamlit Community Cloud
    - Basic deployment workflow explanation
    - Alternative deployment options (Render / Railway / HuggingFace)

📝 Summary:
    - requirements.txt → list of dependencies
    - Streamlit Cloud → easiest free hosting for Streamlit apps
    - GitHub → version control + connection with Streamlit Cloud
    - Other options → Render / Railway / HuggingFace Spaces
"""

# =====================================================
# ================== Introduction =====================
# =====================================================

import streamlit as st

st.title("🚀 Streamlit Deployment & Publishing")
st.write("""
Deploying your Streamlit app means making it publicly accessible — 
so others can view or use your project live, just by visiting a link.
""")

st.header("Why Deploy?")
st.markdown("""
- ✅ Share your work with friends, teachers, or recruiters  
- 🌐 Turn your Python project into a live web app  
- 📊 Host dashboards or ML demos easily  
""")

# =====================================================
# ================== requirements.txt =================
# =====================================================

st.header("Step 1️⃣ - Create requirements.txt")

st.code("""
# In your project folder, run:
pip freeze > requirements.txt
""", language="bash")

st.write("""
This file lists all the libraries your project needs.
When deploying, the server installs these automatically.
""")

# Example of requirements.txt
st.subheader("Example of requirements.txt")
st.code("""
streamlit==1.38.0
pandas
numpy
plotly
altair
matplotlib
seaborn
""", language="text")

# =====================================================
# ================== GitHub Setup =====================
# =====================================================

st.header("Step 2️⃣ - Push Project to GitHub")

st.markdown("""
1. Create a new repository on GitHub  
2. Add your project files (`app.py`, `requirements.txt`, etc.)  
3. Commit and push:
""")

st.code("""
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/streamlit-app.git
git push -u origin main
""", language="bash")

st.info("💡 Tip: Your Streamlit app must be at the root level (not inside folders).")

# =====================================================
# ================== Streamlit Cloud ==================
# =====================================================

st.header("Step 3️⃣ - Deploy on Streamlit Community Cloud")

st.markdown("""
1. Go to [https://share.streamlit.io](https://share.streamlit.io)  
2. Log in with your GitHub account  
3. Click **New App** → select your repo and main file (e.g., `app.py`)  
4. Streamlit automatically builds and deploys your app! 🎉
""")

st.success("✅ Once deployed, you'll get a public link like: https://yourname-yourapp.streamlit.app")

# =====================================================
# ================== Alternatives =====================
# =====================================================

st.header("🌍 Alternative Deployment Options")

st.markdown("""
If you want more control or custom domains, you can use:
- **Render** → Easy Python hosting  
- **Railway** → Free tier for small apps  
- **HuggingFace Spaces** → Ideal for ML demos (supports Streamlit natively)  
- **AWS / Azure / GCP** → For advanced enterprise deployment  
""")

# =====================================================
# ================== Deployment Flow ==================
# =====================================================

st.header("⚙️ Deployment Flow Recap")

st.write("""
1. Develop locally → test using `streamlit run app.py`  
2. Freeze dependencies → `pip freeze > requirements.txt`  
3. Push to GitHub  
4. Connect to Streamlit Cloud  
5. Get live link → share your dashboard/app 🌐
""")

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- requirements.txt → defines dependencies.
- GitHub → stores and versions your project.
- Streamlit Cloud → easiest free deployment option.
- Alternatives → Render, Railway, HuggingFace.
- Deployment Flow → Build → Push → Deploy → Share.
"""
