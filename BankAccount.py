class bankAccount:
    def __init__(self):
        self.full_name = ""
        self.account_number= 0
        self.routing_number =0 
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Amount Deposited: ${amount}"
    
    def withdraw(self, amount):
        self.balance -= amount
        return f"Amount Withdrawn: ${amount}"

    def get_balance(self):
        return f"Hello! Your current balance is: {self.balance}"



account1 = bankAccount()
print(account1.deposit(35))
print(account1.get_balance())
print(account1.withdraw(10))
print(account1.get_balance())