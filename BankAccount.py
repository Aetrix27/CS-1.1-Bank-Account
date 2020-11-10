from random import randint

accessingAccount = True

class bankAccount:

    def __init__(self):
        self.full_name = ""
        randomNum = randint(00000000, 99999999)
        counter = 0
        rand = str(randomNum)
        for num in rand:
            counter +=1
            if (counter < 5):
                rand = rand.replace(num, "*")
             
        self.account_number = rand
        randomNum2 = randint(00000000, 99999999)
        counter2 = 0
        rand2 = str(randomNum2)
        for num in rand2:
            counter2 +=1
            if (counter2 < 5):
                rand2 = rand2.replace(num, "*")
        self.routing_number = rand2
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Amount Deposited: ${amount}"
    
    def withdraw(self, amount):
        calc_balance = self.balance - amount
        if calc_balance < 0:
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

account1 = bankAccount()

while accessingAccount == True:
    selection = int(input("""Please select from the options below by typing the number: \n
        1. Deposit \n
        2. Withdraw \n
        3. Get Balance \n
        4. Add interest \n
        5. Print Receipt \n
        6. Exit \n"""))

    if(selection == 1):
        amount = int(input("How much? \n"))
        print(account1.deposit(amount))
    elif(selection == 2):
        amount = int(input("How much? \n"))
        print(account1.withdraw(amount))
    elif(selection == 3):
        print(account1.get_balance())
    elif(selection == 4):
        account1.add_interest()
    elif(selection == 5):
        print(account1.print_receipt())
    elif(selection == 6):
        accessingAccount = False