from random import randint

class bankAccount:

    def __init__(self):
        self.full_name = ""
        self.account_number = randint(00000000, 99999999)
        self.routing_number = randint(00000000, 99999999)
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

    def print_receipt(self):
        return f"""{self.full_name} \n
                Account No: {self.account_number} \n 
                Routing No: {self.routing_number}\n 
                Balance: ${self.balance}"""


selection = int(input("""Welcome, please select from the options below by typing the number: \n
        1. Deposit \n
        2. Withdraw \n
        3. Get Balance \n
        4. Add interest \n
        5. Print Receipt \n"""))


account1 = bankAccount()
if(selection == 1):
    amount = int(input("How much? \n"))
    print(account1.deposit(amount))
elif(selection ==2):
    amount = int(input("How much? \n"))
    print(account1.withdraw(amount))
elif(selection == 3):
    print(account1.get_balance())
elif(selection == 4):
    account1.add_interest()
elif(selection == 5):
    print(account1.print_receipt())