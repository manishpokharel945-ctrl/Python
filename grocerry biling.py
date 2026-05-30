# Daily Expense Tracker
# A simple Python project to track daily expenses

expenses = []

def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))

    expense = {
        "title": title,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['title']} - Rs. {expense['amount']}")

def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense: Rs. {total}")

def highest_expense():
    if not expenses:
        print("No expenses found.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\n--- Highest Expense ---")
    print(f"Title: {highest['title']}")
    print(f"Amount: Rs. {highest['amount']}")

while True:
    print("\n===== Daily Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Highest Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        highest_expense()
    elif choice == "5":
        print("Thank you for using Daily Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")