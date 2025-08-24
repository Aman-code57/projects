class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount}. Current balance: {self.balance}")
            else:
                print("Insufficient balance!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"


class SavingsAccount(Account):
    def interest(self):
        print("Savings account earns 5% annual interest.")


class CurrentAccount(Account):
    def overdraft(self):
        print("Current account allows overdraft facility.")


def main():
    print("Welcome to the Bank!")
    name = input("Enter your name: ")

    print("\nChoose Account Type:")
    print("1. Savings Account")
    print("2. Current Account")

    acc_type = input("Enter your choice (1 or 2): ")

    if acc_type == '1':
        account = SavingsAccount(name)
    elif acc_type == '2':
        account = CurrentAccount(name)
    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Account Info")
        print("4. Account Feature Info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account.deposit()
        elif choice == '2':
            account.withdraw()
        elif choice == '3':
            print(account)
        elif choice == '4':
            if isinstance(account, SavingsAccount):
                account.interest()
            elif isinstance(account, CurrentAccount):
                account.overdraft()
        elif choice == '5':
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
