"""
This is my Expense Tracker project.
I built it using basic Python concepts like:
- File I/O
- Dictionaries,list
- match-case statements
- Function definitions and many more

Created on Day-17 (24-Aug-2025)
"""


import os       # just for file exchange


class invalidAnswerError(Exception):
    pass


def add_expense():
    print("{:^50}".format("-----Add expense-----"))
    title = input("What is your title? ")
    title = title.replace(" ", "_")
    expense = input("What is your expense? ")
    if not expense.isdigit():
        print("Invalid Answer, Expense must be numeric")
        raise invalidAnswerError
    expense = int(expense)
    catList = viewCategory()
    while True:
        try:
            category = int(input("In what category do you want to add the expense? (1,2,3...)"))
            try:
                if category < 0 or category > len(catList):
                    raise invalidAnswerError
            except invalidAnswerError:
                print("Invalid Answer")
                continue
            break
        except ValueError:
            print("Invalid Answer, select number of the category.")

    with open("yourExpense.txt", "a") as add:
        add.write(f"{title} : {expense} ₹ {catList[category - 1]}\n")
        print("Your expense was added.")


def view_expense():
    print("{:^50}".format("-----View expense-----"))
    print("Your expense is\n")
    with open("yourExpense.txt", "r") as view:
        i = 1
        print("{:<5} {:<12} {:>12} {:>10}".format("No.", "Title", "Expense", "Category"),
              end="\n-------------------------------------------\n")
        while True:
            line = view.readline()
            if not line:
                break
            # print("{:<10}".format(f"{i} -> "),"{:^10}".format(line.split(":")[0]),"{:>10}".format(line.split(":")[1]))
            print(
                "{:<6} {:<15} {:<1} {:>10} {:<1} {:^10}".format(
                    f"{i} -> ",
                    f"{line.split(" ")[0].strip()}",
                    f"{line.split(" ")[1].strip()}",
                    f"{line.split(" ")[2].strip()}",
                    f"{line.split(" ")[3].strip()}",
                    f"{line.split(" ")[4].strip()}")
            )
            i += 1


def edit_expense():
    print("{:^50}".format("-----Edit expense-----"))
    dictionary = {}
    # Read existing expenses into a dictionary with (expense, category) tuple
    with open("yourExpense.txt", "r") as edit_expense:
        while True:
            line = edit_expense.readline()
            if not line:
                break
            title = line.split(" ")[0].strip()
            expense = line.split(" ")[2].strip()
            category = line.split(" ")[4].strip()
            dictionary[title] = (expense, category)

    title = input("Enter your title for edit expense: ")
    try:
        print(f"it's expense was : {dictionary[title][0]} ₹, Category: {dictionary[title][1]}")
    except KeyError:
        print("No such title exists, If you want to add title then choose 1 in menu!!")
        return

    newValue = input("Enter new value for your expense: ")
    if not newValue.isdigit():
        print("Invalid Answer, Expense must be numeric")
        raise invalidAnswerError

    dictionary[title] = (int(newValue), dictionary[title][1])
    print("Your expense was edited.")

    # NOTE: Directly rewriting the expense file can cause data loss if the system crashes mid-write.
    # To prevent this, we first write changes to a temporary file.
    # Only after a successful write do we replace the main file, ensuring previous data is not lost.
    with open("temp.txt", "w") as temp:
        for key, (value, cat) in dictionary.items():
            temp.write(f"{key} : {value} ₹ {cat}\n")
    os.replace("temp.txt", "yourExpense.txt")  # replace old file with temp file


def delete_expense():
    print("{:^50}".format("-----Delete expense-----"))
    title = input("Enter title to delete expense: ")
    dictionary = {}

    # Read existing expenses into a dictionary with (expense, category) tuple
    with open("yourExpense.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_title = line.split(" ")[0].strip()
            expense = line.split(" ")[2].strip()
            category = line.split(" ")[4].strip()  # preserve category
            dictionary[line_title] = (expense, category)

    try:
        print(f"it's expense was : {dictionary[title][0]} ₹, Category: {dictionary[title][1]}")
    except KeyError:
        print("No such title exists, If you want to add title then choose 1 in menu!!")
        return

    while True:
        try:
            ans = input(f"Are you sure you want to delete '{title}'? (Y/N): ")
            if ans.upper() not in ("Y", "N"):
                raise invalidAnswerError
            elif ans.upper() != "Y":
                print("Deletion cancelled.")
                return
            elif ans.upper() == "Y":
                break
        except invalidAnswerError:
            print("Invalid Answer.\n Please enter Y or N, Y for Yes, N for No")

    dictionary.pop(title)
    print("Your expense was deleted.")

    #------- Same safe-write logic as Edit -------
    # NOTE: Directly rewriting the expense file can cause data loss if the system crashes mid-write.
    # To prevent this, we first write changes to a temporary file.
    # Only after a successful write do we replace the main file, ensuring previous data is not lost.
    with open("temp.txt", "w") as temp:
        for key, (value, cat) in dictionary.items():
            temp.write(f"{key} : {value} ₹ {cat}\n")
    os.replace("temp.txt", "yourExpense.txt")  # replace old file with temp file



def countExpense():
    print("{:^50}".format("-----Total expense-----"))
    view_expense()
    catList = viewCategory()
    while True:
        try:
            select = int(input("Give category Number(1,2,3...) for expense or write \'0\' for Grand total of expense for all categories: "))
            if select < 0 or select > len(catList):
                raise invalidAnswerError
            break
        except invalidAnswerError | ValueError:
            print("Invalid Answer. Please enter number between given list")

    with open("yourExpense.txt", "r") as exp:
        if select == 0:
            # Grand total
            lst = [int(line.split(" ")[2].strip()) for line in exp]
        else:
            # Category-wise total
            lst = [int(line.split(" ")[2].strip()) for line in exp if line.split(" ")[4].strip() == catList[select - 1]]

        sum = 0
        for value in lst:
            sum += value

        print("{:<10} {:>10}".format("Category", "Expense"), end="\n---------------------\n")
        if select == 0:
            print("{:<10} {:>10}".format("Grand Total", f"- {sum} ₹"))
        else:
            print("{:<10} {:>10}".format(catList[select - 1], f"- {sum} ₹"))


def addCategory():
    print("{:^50}".format("-----Add Category-----"))
    newCat = input('Enter name of the Category: ')
    with open("categories.txt", "a") as cat:
        cat.write(f"{newCat}\n")
    print("Category added successfully.")


def viewCategory():
    print("{:^50}".format("-----View Category-----"))
    with open("categories.txt", "r") as cat:
        categories = [line.strip() for line in cat.readlines() if line.strip()]
        # NOTE: can also do for line in cat if line.strip()...
    for x, cat in enumerate(categories, 1):
        print(f"{x}) {cat}")
    return categories


print("{:^50}".format("Welcome to expense tracker"))
print("{:^50}".format("Menu"))
print("{:^50}".format("------------------"))
print("{:^50}".format("1.Add Expense"))
print("{:^50}".format("2.View Expense"))
print("{:^50}".format("3.Edit Expense"))
print("{:^50}".format("4.Delete Expense"))
print("{:^50}".format("5.Total Expense"))
print("{:^50}".format("6.Add new category"))
print("{:^50}".format("7.View category"))
print("{:^50}".format("8.Exit"))

while True:
    choice = int(input("Enter your choice: "))

    match (choice):
        case 1:
            add_expense()
        case 2:
            view_expense()
        case 3:
            edit_expense()
        case 4:
            delete_expense()
        case 5:
            countExpense()
        case 6:
            addCategory()
        case 7:
            viewCategory()
        case 8:
            print("Thank you for using expense tracker")
            break