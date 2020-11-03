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
        calc_balance = self.balance - amount
        if calc_balance > self.balance:
            return "Insufficent Funds!"
        else:
            self.balance -= amount

        return f"Amount Withdrawn: ${amount}"

    def get_balance(self):
        return f"Hello! Your current balance is: {self.balance}"

    def add_interest(self):
        monthly_interest = self.balance *  0.0008
        self.balance *= monthly_interest
        return self.balance



account1 = bankAccount()
print(account1.deposit(35))
account1.add_interest()
print(account1.get_balance())
print(account1.withdraw(10))
print(account1.get_balance())