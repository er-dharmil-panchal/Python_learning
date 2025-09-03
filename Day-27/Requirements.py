"""
📌 Requirements.txt
    - It’s a plain text file that lists all the Python packages your project needs, along with their versions.
    - Example:
        - requests==2.31.0
        - jsonschema==4.18.0
        - flask==2.3.2
    - It ensures that anyone running your project can install the exact same packages you used.
    - This file can be used to easily install all the required packages in a new environment.
"""

"""
Why use requirements.txt?
    - Reproducibility: Your project will work the same on another computer, server, or collaborator’s machine.
    - Easy installation: Instead of installing packages one by one, you can install all dependencies with one command.
    - Version control: You lock the package versions, so updates to packages won’t break your project unexpectedly.
"""

"""
How to create requirements.txt
    Step 1: Activate your virtual environment

    Step 2: Install any packages you need
        pip install requests
        pip install jsonschema

    Step 3: Generate requirements.txt
        pip freeze > requirements.txt
        - This creates a file with all currently installed packages and their versions in your venv.
        Example content:
            attrs==25.3.0
            certifi==2025.8.3
            charset-normalizer==3.4.3
            idna==3.10
            jsonschema==4.25.1
            jsonschema-specifications==2025.4.1
            referencing==0.36.2
            requests==2.32.5
            rpds-py==0.27.1
            urllib3==2.5.0
"""

"""
How to install from requirements.txt
    - If you share your project or move to another machine:
        1. Clone or copy your project.
        2. Create a virtual environment.
        3. Run this command (requirements.txt is the file from above):
            pip install -r requirements.txt
    - To update requirements.txt after installing/updating packages:
        pip freeze > requirements.txt
"""

# NOTE:
#   - Keep requirements.txt in your project root folder.
#   - Only include packages your project actually uses.
#   - Don’t include system packages or libraries installed globally outside the venv.

"""
Summary
    - requirements.txt = a snapshot of your project’s Python environment.
    - Easy to share, recreate, and maintain your project dependencies.
    - Works hand-in-hand with virtual environments.
"""
