##Bank Account Manager Project 

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, fee=1):
        super().__init__(account_number, balance)
        self.fee = fee

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        total_withdrawal = amount + self.fee
        if total_withdrawal > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= total_withdrawal

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def add_interest(self):
        self.balance *= (1 + self.interest_rate)

class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, transaction_fee=0.5, monthly_fee=5):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee
        self.monthly_fee = monthly_fee
        self.num_transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.num_transactions += 1

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            total_withdrawal = amount + self.transaction_fee
            self.balance -= total_withdrawal
            self.num_transactions += 1

    def deduct_monthly_fee(self):
        num_free_transactions = 50
        if self.num_transactions > num_free_transactions:
            extra_transactions = self.num_transactions - num_free_transactions
            total_fee = self.monthly_fee + (extra_transactions * self.transaction_fee)
        else:
            total_fee = self.monthly_fee
        self.balance -= total_fee
        self.num_transactions = 0

# Ask the user for the account type
account_type = input("Enter account type (Checking, Savings, or Business): ").strip().capitalize()

# Initialize account as None
account = None

# Create the selected account with user-defined initial balance
if account_type == "Checking":
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = CheckingAccount(account_number, initial_balance)
elif account_type == "Savings":
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = SavingsAccount(account_number, initial_balance)
elif account_type == "Business":
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BusinessAccount(account_number, initial_balance)
else:
    print("Invalid account type")

# Perform deposit and withdrawal operations
if account:
    deposit_amount = float(input("Enter deposit amount: "))
    account.deposit(deposit_amount)

    withdrawal_amount = float(input("Enter withdrawal amount: "))
    account.withdraw(withdrawal_amount)

    # Display updated account balance
    print(f"{account_type} account balance:", account.get_balance())
