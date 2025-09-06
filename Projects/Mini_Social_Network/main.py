"""
Main.py for user input and operation perform
"""
from colorama import Fore, Style, init
from time1 import strftime
from user import User
import hashlib
import Util as ut
import Post as p
from Social_Network import Social_Network as sn


def mainMenu(user):
    init(autoreset=True)
    while True:
        print("\n" + "=" * 125)
        print(f"{'🌟 MAIN MENU 🌟':^{125}}")
        print("=" * 125 + "\n")

        print("{:^50} {:<10} {:<10}".format(" ", "1.", "📰 View Feed"))
        print("{:^50} {:<10} {:<10}".format(" ", "2.", "✏️ Create Post"))
        print("{:^50} {:<10} {:<10}".format(" ", "3.", "🔍 Search User"))
        print("{:^50} {:<10} {:<10}".format(" ", "4.", "👤 View Profile"))
        print("{:^50} {:<10} {:<10}".format(" ", "5.", Fore.RED + "🚪 Logout" + Style.RESET_ALL))

        print("\n" + "=" * 125 + "\n")

        try:
            choice = int(input("Enter your choice : "))
            match choice:
                case 1:
                    feed = sn.get_feed(user)
                    ut.display_feed(feed)
                case 2:
                    print("\n📝 --- Create a New Post --- 📝\n")
                    title = input("🖊️ Title: ").strip()
                    content = input("🗒️ Content: ").strip()
                    created_at = strftime("(%c)")
                    Post = p.Post(title, content, user.username, created_at)
                    Post.create_post()
                    print("✔ Post created successfully!!")
                case 3:
                    print("\n🔍 --- Search for a User --- 🔍\n")
                    FindUser = input("👤 Enter the username to search: ").strip()
                    searched_user = User.from_dict(ut.search_user(FindUser))
                    if searched_user:
                        print("✔ User found!!")
                        ut.display_profile(user, searched_user)
                    else:
                        print("✖ User not found!!, try again")
                case 4:
                    print("\n👤 --- View Profile --- 👤\n")
                    ut.display_profile(user, user)
                case 5:
                    print("🚪 Logging out...")
                    break
                case _:
                    print("⚠️ Please enter a number between 1 and 5!")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")


print("═" * 125, "\n")
print(f"{Style.BRIGHT + '🙏🏻  WELCOME TO MINI SOCIAL NETWORK  🌐' + Style.RESET_ALL:^{135}}", "\n")
print("═" * 125)


# Menu
def menu():
    from colorama import Fore, Style, init
    init(autoreset=True)
    print("{:^125}".format("🌐 MINI SOCIAL NETWORK"))
    print("=" * 125)
    print("{:^50} {:<5} {:<10}".format(" ", "1.", "📝 Register"))
    print("{:^50} {:<5} {:<10}".format(" ", "2.", "🔑 Login"))
    print("{:^50} {:<5} {:<10}".format(" ", "3.", Fore.RED + "🚪 Exit" + Style.RESET_ALL))
    print("=" * 125)

Flag = True
while Flag:
    menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 3:
            print("⚠️ Please enter a number between 1 and 3!")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue
    match (choice):
        case 1:
            print("\n" + "─" * 125)
            print(f"{'📝 Registration':^{125}}")
            print("─" * 125 + "\n")
            username = input(f"👤 Enter your username for the account: ").strip()
            while True:
                if ut.check_username(username):
                    username = input("⚠️  Username already exists. Please enter another username: ").strip()
                else:
                    break
            while (True):
                password = input("🔑 Please enter your password for the account: ")
                confirmPassword = input("🔑 Confirm your password: ")
                if password != confirmPassword:
                    print("⚠ Passwords do not match!")
                else:
                    print("✔ Password created successfully!")
                    break
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            while (True):
                try:
                    age = int(input("Please enter your age : "))
                    if (age <= 0):
                        raise ut.ageError("Age must be greater than 0")
                    break
                except ValueError:
                    print("Enter a valid age")
                except ut.ageError as e:
                    print(e)

            bio = input("📝 Please enter your bio (press Enter to skip): ")
            created_at = strftime("(%c)")
            user = User(username, hashed_password, age, bio, created_at)
            user.register()
            print(f"🎉 Your account was created successfully! ({created_at})")
            sn.update_followers(user)
            mainMenu(user)
            pass
        case 2:
            print("Login")
            username = input("👤 Please enter your username for login: ").strip()
            password = input("🔑 Please enter your password for login: ").strip()
            user = ut.login_verification(username, password)
            if user:
                user_login = User(user['username'], user['password'], user['age'], user['bio'], user['created_at'])
                user_login.login()
                print("✔ Login Successful")
                mainMenu(user_login)
            else:
                print("✖ Login Failed! Please try again")
        case 3:
            Flag = False
            print("👋 Thanks for using MINI SOCIAL NETWORK! Goodbye!")
            break
