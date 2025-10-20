class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds.....")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount}. Balance {self.balance}........")

acc_1 = BankAccount("Al-Farhan")
acc_1.deposit(25000)
acc_1.withdraw(250000)
acc_1.deposit(300000)
acc_1.withdraw(20000)