# 🌐 Mini Social Network

A **Python command-line application** to simulate a social networking platform, built as part of my Python learning journey.

---

## 🌟 Features

- **User Registration & Login** – Secure system with SHA-256 password hashing.  
- **Profile Management** – Basic profile setup with username, age, and bio.  
- **Post Creation** – Users can create posts with title, content, and timestamps.  
- **Follow/Unfollow System** – Follow other users and manage your social connections.  
- **Dynamic Feed** – See posts from followed users first, sorted by most recent.  
- **Persistent Storage** – Data stored in JSON files (`users.json`, `posts.json`, `followers.json`).  
- **Input Validation & CLI Navigation** – Prevent invalid actions and provide a clean, interactive menu.  

---

## 🛠 Technical Highlights

- **JSON File Handling** – Store and retrieve user, post, and follower data.  
- **Schema Validation** – Ensures consistent data format with `jsonschema`.  
- **Modular Code Structure** – Separate files for `Main.py`, `user.py`, `Post.py`, `Social_Network.py`, and `Util.py`.  
- **Control Flow** – Menu-driven CLI using `while True` loops and `match-case`.  
- **Exception Handling** – Custom errors for invalid inputs, e.g., age validation.  
- **Time Management** – Timestamp posts with Python’s `strftime`.  

---

🎯 Learning Goals

Created on **Day 29 (05-Sep-2025)** and extended on **Day 30 (06-Sep-2025)** as part of my Python learning journey. This project helped me:

- Structure a CLI project with multiple modules.  
- Handle persistent data storage safely with JSON files.  
- Implement social interactions like follow/unfollow and feed prioritization.  
- Validate data formats using `jsonschema`.  
- Build an interactive, menu-driven command-line application.
