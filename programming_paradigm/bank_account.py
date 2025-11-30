# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrawn: {amount}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: {self.account_balance}")
