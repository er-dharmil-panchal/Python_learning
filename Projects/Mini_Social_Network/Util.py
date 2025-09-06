import json
import hashlib
from colorama import Fore, Style
from Post import Post
from Social_Network import Social_Network as sn

def check_username(username):
    data = load_users()
    return any(user['username'] == username for user in data)

def login_verification(username, password):
    data = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = next((u for u in data if u['username'] == username and u['password'] == hashed_password), None)
    return user

@staticmethod
def load_users():
    try:
        with open("Data/users.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        data = []
    return data

@staticmethod
def load_posts():
    try:
        with open("Data/posts.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        data = []
    return data

@staticmethod
def load_followers():
    try:
        with open("Data/followers.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        data = []
    return data

@staticmethod
def search_user(username):
    data = load_users()
    for user in data:
        if user['username'] == username:
            return user

def display_feed(feed):
    print("=" * 100)
    print("{:^100}".format(f"{Fore.LIGHTWHITE_EX}📢 SOCIAL FEED"))
    print("=" * 100)

    if not feed:
        print("{:^100}".format("😕 No posts to show yet..."))
        print("=" * 100)
        return

    for idx, post in enumerate(feed, start=1):
        print(f"   {Fore.GREEN}{Style.BRIGHT}👤 {post.username}{Style.RESET_ALL}   |   {Fore.MAGENTA}{post.created_at}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{idx}. {Style.RESET_ALL}{Fore.LIGHTWHITE_EX}🏷 {post.title} - {Fore.LIGHTWHITE_EX}{Style.BRIGHT}{post.content}{Style.RESET_ALL}")
        print("-" * 100)
"""
Exception classes
"""
class ageError(Exception):
    pass


def display_profile(current_user,searched_user):
    print("\n" + "=" * 40)
    print(f"👤 PROFILE: {searched_user.username}")
    print("=" * 40)
    print(f"Age: {searched_user.age}")
    print(f"Bio: {searched_user.bio if searched_user.bio else 'No bio added yet.'}")
    print("-" * 40)

    # Determine current follow state
    if current_user is not searched_user:
        action = "Unfollow" if sn.is_following(current_user, searched_user) else "Follow"
        print(f"[1] {action} this user")
        print("[0] Go Back")
        print("=" * 40 + "\n")
    posts = Post.get_post_by_username(searched_user.username)
    if posts:
        print("📜 Recent Posts:")
        for idx, post in enumerate(posts[-5:], 1):  # last 5 posts
            print(f"{idx}. {post.title} – {post.content} (Posted on: {post.created_at})")
    else:
        print("No posts yet.")
    print("-" * 40)
    if current_user is not searched_user:
        choice = input("Enter your choice (From 1 and 0): ")
        if choice == "1":
            sn.update_followers(current_user, searched_user,action)
            if current_user.username != searched_user.username:
                print(f"✔ You have {action.lower()}ed {searched_user.username}")
        return None
    input("Press Enter to go back...")
    return None