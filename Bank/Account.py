from Class_unittest_more.Bank.BankException import BankException

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.minimumBalance = 10

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if (amount < 0):
            raise BankException("Error the amount must be positive")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if (amount < 0):
            raise BankException("Error the amount must be positive")
        if (self.balance -amount < self.minimumBalance):
            raise BankException("Error insufficient funds in the account")
        self.balance = self.balance - amount

    def transferFunds(self, destination, amount):
        if (self.balance -amount < self.minimumBalance):
            raise BankException("Error, balance is minor than minimum balance")
        destination.deposit(amount)
        self.withdraw(amount)
