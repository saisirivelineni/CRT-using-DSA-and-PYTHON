class BankAccount:
    def __init__(self, holder, balance):
        self.account_holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print("Balance:", self.balance)

a = BankAccount("Ravi", 5000)
a.deposit(1000)
a.withdraw(500)
a.check_balance()