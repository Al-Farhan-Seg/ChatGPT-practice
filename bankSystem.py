class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount MUST be positive...."
        else:
            self.balance += amount
            self.transactions.append({"Transaction":"Deposit",
                                      "Amount":amount,
                                      "Balance after": self.balance })

        return f"You have successfully deposited {amount}. New Balance {self.balance}........"
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds.....")
        else:
            self.balance -= amount
            self.transactions.append({"Transaction":"Withdraw",
                                      "Amount":amount,
                                      "Balance after": self.balance })
            return f"You have successfully withdrawn {amount}. New Balance {self.balance}........"

acc_1 = BankAccount("Al-Farhan")
acc_1.deposit(25000)
acc_1.withdraw(250000)
acc_1.deposit(300000)
acc_1.withdraw(20000)