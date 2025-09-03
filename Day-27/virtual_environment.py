"""
 📌 Virtual environment
        - A virtual environment in Python is an isolated workspace for your Python project
        - allowing you to work on multiple projects with different dependencies and packages without conflicts
        - Have a separate Python interpreter for each project
        - install project-specific libraries without affecting your system-wide Python.
        - Avoid version conflicts between projects (Example :- one project needs Django 3.2 and another needs Django 4.2)
"""

# Why we do need virtual environment ???
"""
    Imagine :- 
        Project A needs numpy 1.23.
        Project B needs numpy 1.25.
        If you install packages 'globally', you can’t satisfy both projects at the same time. 
        Virtual environments solve this problem by keeping 'packages isolated per project'.
"""

# -------------------------------
# How to Create a Python Virtual Environment
# -------------------------------

# Step 1: Go to your project folder
# Open your terminal and navigate to your project folder
# Example (Mac/Linux):
# cd path/to/your/project
# Example (Windows CMD):
# cd C:\path\to\your\project

# Step 2: Create the virtual environment
# If you have Python 3 installed, run:
# python3 -m venv myvenv
# Replace 'myvenv' with your desired environment name
# If your Python version is different, use that version:
# python3.11 -m venv myvenv

# This creates a folder called 'myvenv' inside your project folder
# which contains a self-contained Python environment.

# Step 3: Activate the virtual environment

# On macOS / Linux:
# source myvenv/bin/activate

# On Windows (Command Prompt):
# myvenv\Scripts\activate

# On Windows (PowerShell):
# myvenv\Scripts\Activate.ps1

# After activation, your terminal will show the environment name in parentheses, e.g., (myvenv)
# This means your virtual environment is active.

# Step 4: Install packages (optional)
# While the virtual environment is active, install any packages you need using pip:
# pip install requests
# pip install jsonschema
# These packages will only be installed inside this environment and will not affect other projects.

# Step 5: Deactivate the virtual environment
# When you're done working, you can deactivate the environment:
# deactivate
# Your terminal will return to the system Python.
# If you want to activate again just follow step 3 again..

# Step 6: Delete the virtual environment (if you no longer need it)
# Make sure it is deactivated first
# Remove the environment folder completely:
# Mac/Linux:
# rm -rf myvenv
# Windows CMD:
# rmdir /s /q myvenv
# Windows PowerShell:
# Remove-Item -Recurse -Force myvenv
# This deletes all installed packages in the environment. Your project files remain safe.


# -------------------------------
# Multiple Virtual Environments
# -------------------------------

# You can have multiple virtual environments on your system.
# Example:
# project1/venv1
# socialnet/socialnet_venv
# project2/venv2
# Each environment is isolated and has its own packages.

# Only one virtual environment can be active per terminal session.
# Example of multiple terminals:
# Terminal 1:
# cd socialnet
# source socialnet_venv/bin/activate   # (socialnet_venv) active
# Terminal 2:
# cd project2
# source venv2/bin/activate            # (venv2) active

# To switch environments in the same terminal:
# deactivate                           # deactivate current venv
# source another_venv/bin/activate     # activate a different venv

# IDEs like PyCharm allow you to configure a virtual environment per project,
# so you can work with multiple environments “at once” by opening different projects
# or windows, each using its own virtual environment.
