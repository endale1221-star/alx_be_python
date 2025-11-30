class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # EXACT format required by your test
        line = f"Current Balance: ${self.account_balance:.2f}"
        print(line)
        return line
