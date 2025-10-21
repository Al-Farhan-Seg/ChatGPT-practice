from datetime import datetime
import string, random
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def trans_ID(self):
        
        return "TXN-" + ''.join(random.sample(string.ascii_letters + string.digits, 10))

        

    def deposit(self, amount):
        if amount <= 0:
            return "\nDeposit amount MUST be positive...."
        else:
            self.balance += amount
            ID = self.trans_ID()
            self.transactions.append({"Transaction":"Deposit",
                                      "ID":ID,
                                      "Amount":amount,
                                      "Balance after": self.balance, 
                                      "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")})

        return f"""\nDeposited: {amount}
New Balance: {self.balance}
Transaction ID: {ID}"""
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "\nYou have insufficient funds....."
        else:
            self.balance -= amount
            ID = self.trans_ID()
            self.transactions.append({"Transaction":"Withdraw",
                                      "ID":ID,
                                      "Amount":amount,
                                      "Balance after": self.balance, 
                                      "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")})
            
            return f"""\nWithdrawn: {amount}
New Balance: {self.balance}
Transaction ID: {ID}"""

acc_1 = BankAccount("Al-Farhan")
print(acc_1.deposit(25000))
print(acc_1.withdraw(250000))
print(acc_1.deposit(300000))
print(acc_1.withdraw(20000))
#datetime.now()