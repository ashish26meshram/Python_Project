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

# Create accounts with user-defined initial balances
checking = CheckingAccount("1234", float(input("Enter initial balance for Checking account: ")))
savings = SavingsAccount("5678", float(input("Enter initial balance for Savings account: ")))
business = BusinessAccount("9012", float(input("Enter initial balance for Business account: ")))

# Deposit and withdraw money with user input
checking.deposit(float(input("Enter deposit amount for Checking account: ")))
savings.deposit(float(input("Enter deposit amount for Savings account: ")))
business.deposit(float(input("Enter deposit amount for Business account: ")))

checking.withdraw(float(input("Enter withdrawal amount for Checking account: ")))
savings.withdraw(float(input("Enter withdrawal amount for Savings account: ")))
business.withdraw(float(input("Enter withdrawal amount for Business account: ")))

# Display account balances
print("Checking account balance:", checking.get_balance())
print("Savings account balance:", savings.get_balance())
print("Business account balance:", business.get_balance())

# Add interest and deduct monthly fees (if applicable)
savings.add_interest()
business.deduct_monthly_fee()

# Display updated account balances
print("Checking account balance:", checking.get_balance())
print("Savings account balance:", savings.get_balance())
print("Business account balance:", business.get_balance())
