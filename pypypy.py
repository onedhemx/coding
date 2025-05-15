class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"пополнено: {amount}")
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f"cнято: {amount}")
        
    def get_balance(self):
            return self.balance
    
    def get_account_number(self):
            return self.account_number
        
        
account_number = BankAccount("12345678922288889909096543423211", 1000.666)
print("текущий баланс:", account_number.get_balance())

