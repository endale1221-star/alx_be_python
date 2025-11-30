# bank_account.py

class BankAccount:
    """
    Simple bank account class:
      - account_balance stored as a float
      - deposit(amount) -> returns new balance (float)
      - withdraw(amount) -> returns True if successful, False if insufficient funds
      - display_balance() -> prints a single line and returns the same string
    """

    def __init__(self, initial_balance=0):
        try:
            self.account_balance = float(initial_balance)
        except (TypeError, ValueError):
            raise ValueError("Initial balance must be a number.")
    
    def deposit(self, amount):
        """
        Add amount to account_balance and return new balance.
        Raises ValueError if amount is not a positive number.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a number.")
        if amt <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amt
        return self.account_balance

    def withdraw(self, amount):
        """
        Attempt to withdraw amount.
        Returns True and deducts amount if sufficient funds and amount positive.
        Returns False (and does not change balance) if insufficient funds.
        Raises ValueError if amount is not a positive number.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdrawal amount must be a number.")
        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.account_balance >= amt:
            self.account_balance -= amt
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current balance in a single, exact line and return that string.
        Format: "Current Balance: <balance>"
        Balance uses plain representation (no currency symbol) so tests comparing text can be precise.
        """
        line = f"Current Balance: {self.account_balance}"
        print(line)
        return line

    def __str__(self):
        return f"BankAccount(balance={self.account_balance})"
