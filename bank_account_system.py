class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: Rs. {amount}")
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: Rs. {amount}")
            print(f"Rs. {amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: Rs. {self.balance}")

    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Rs. {self.balance}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


def main():
    print("Welcome to Python Bank Account System")

    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(name, account_number, initial_balance)

    while True:
        print("\n===== Bank Menu =====")
        print("1. Show Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Show Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.show_details()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "4":
            account.check_balance()

        elif choice == "5":
            account.show_transactions()

        elif choice == "6":
            print("Thank you for using Python Bank Account System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()