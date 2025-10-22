from datetime import datetime
import string, random
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
        self.__transactions = []
        self.__pin = 1

    def trans_ID(self):
        return "TXN-" + ''.join(random.sample(string.ascii_letters + string.digits, 10))
  

    def deposit(self, amount):
        print("ACCOUNT DEPOSIT Management".center(50, "_"))
        attempts = 0

        # to limit number of PIN input attempts to 3
        while attempts < 3:
            depo = self._verify_pin(attempts)
            if depo == True:
                if amount <= 0:
                        return "\nDeposit amount MUST be positive...."
                else:
                    self.__balance += amount
                    ID = self.trans_ID()

                    # Storing the transaction details into the Transaction Log
                    self.__transactions.append({"Transaction":"Deposit",
                                            "ID":ID,
                                            "Amount":amount,
                                            "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")})

                    return f"""\nDeposited: {amount}
Transaction ID: {ID}"""
            elif depo == False:
                attempts += 1
            else:
                print(depo)
        
        return "Too many Failed attempts" 
    
    def withdraw(self, amount):
        print("ACCOUNT WITHDRAWAL Management".center(50, "_"))
        attempts = 0

        # to limit number of PIN input attempts to 3
        while attempts < 3:
            w_draw = self._verify_pin(attempts)
            if w_draw == True:
                if amount > self.__balance:
                    return "\nYou have insufficient funds....."
                else:
                    self.__balance -= amount
                    ID = self.trans_ID()

                    # Storing the transaction details into the Transaction Log
                    self.__transactions.append({"Transaction":"Withdraw",
                                            "ID":ID,
                                            "Amount":amount,
                                            "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")})
                    
                    return f"""\nWithdrawn: {amount}
Transaction ID: {ID}"""
            elif w_draw == False:
                attempts += 1
            else:
                print(w_draw)

        return "Too many Failed attempts"
    
        
    def display_balance(self):
        print("Balance Display".center(50, "_"))
        attempts = 0

        # to limit number of PIN input attempts to 3
        while attempts < 3:
            bal_disp = self._verify_pin(attempts)
            if bal_disp == True:
                return f"Account Balance: {self.__balance}"
            elif bal_disp == False:
                attempts += 1
            else:
                print(bal_disp)
        
        return "Too Many Failed Attempts"
    
    
    def get_transactions_1(self):
        print("TRANSACTION HISTORY".center(40, "_"))
        for i in self.__transactions:
            print(" ".ljust(15, "_") + " " + " ".rjust(22, "_"))
            print("| TITLE".ljust(15, " ") + "|" + "VALUE".rjust(20, " ") + " |")
            print(" ".ljust(15, "-") + " " + " ".rjust(22, "-"))
            for k,v in i.items():
                print(f"| {k}".ljust(15, " ") + "|" + f"{v}".rjust(20, " ") + " |")
            print(" ".ljust(15, "-") + " " + " ".rjust(22, "-"))
            print()


    def change_pin(self):
        print("PIN CHANGE Management".center(50, "_"))
        attempts = 0
        # to limit the number of PIN input attempts to 3
        while attempts < 3:
            change = self._verify_pin(attempts)
            if change == True:
                new_pin = int(input("Enter NEW account PIN: "))
                self.__pin = new_pin
                return f"PIN successfully changed"
            elif change == False:
                attempts += 1
            else:
                print(change)

        return "Too Many Failed Attempts"
    
    def _verify_pin(self, attempts):
        try:
            pin = int(input("Enter account PIN: "))
            if pin != self.__pin:
                # attempts += 1
                print("PIN incorrect")
                return False
            else:
                return True
        # to catch any non-integer INPUTS
        except ValueError:
            return "PIN must only be an integer"
    

class SavingsAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)

# I dont know how to implememnt this
class CurrentAccount(BankAccount):
    pass

            

acc_1 = BankAccount("Al-Farhan")
print(acc_1.deposit(25000))
print()
print(acc_1.display_balance())
print()
print(acc_1.withdraw(250000))
print()
print(acc_1.deposit(300000))
print()
print(acc_1.withdraw(20000))
print()

print(acc_1.change_pin())
print()
print(acc_1.deposit(27000))
print()
print(acc_1.withdraw(320000))
print()

print(acc_1.display_balance())

acc_1.get_transactions_1()