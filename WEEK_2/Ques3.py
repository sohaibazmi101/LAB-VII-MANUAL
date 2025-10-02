class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: {amount}. Total Balance: {self._balance}")
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Amount {amount} has been withdrawn. Total Available balance: {self._balance}")
        else:
            print("Insuffient Balance")
bankAccount = BankAccount(991290129)
bankAccount.deposit(500)
bankAccount.withdraw(200)
bankAccount.withdraw(400)