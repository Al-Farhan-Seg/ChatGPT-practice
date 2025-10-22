from datetime import datetime
import string, random, csv
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
        self.__transactions = []
        self.__pin = 1
        self.__csv = [[" ", self.owner, "", " "],
                      ["Amount", "Time", "Transaction", "ID"]]

    def trans_ID(self):
        return "TXN-" + ''.join(random.sample(string.ascii_letters + string.digits, 10))
    
    # putting transactions into a .csv file
    def _csv_write(self, info):

        file_path = rf"{self.owner}_transactions.csv"

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            for row in info:
                writer.writerow(row)
            

  

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
                    info = {"Transaction":"Deposit",
                                            "ID":ID,
                                            "Amount":amount,
                                            "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}
                    # Storing the transaction details into the Transaction Log
                    self.__transactions.append(info)
                    info_list = [amount, info["Time"], "Deposit", ID]
                    self.__csv.append(info_list)

                    self._csv_write(self.__csv)

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
                    info = {"Transaction":"Withdraw",
                                            "ID":ID,
                                            "Amount":amount,
                                            "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}

                    # Storing the transaction details into the Transaction Log
                    self.__transactions.append(info)
                    info_list = [amount, info["Time"], "Withdraw", ID]
                    self.__csv.append(info_list)

                    self._csv_write(self.__csv)
                    
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
        attempts = 0
        while attempts < 3:
            type = input("Choose transaction type ('Withdraw' or 'Deposit'): ")
            type = type.capitalize()
            types = ["Withdraw", "Deposit"]
            if type in types:
                for i in self.__transactions:
                    if type in i.values():
                        print(" ".ljust(15, "_") + " " + " ".rjust(22, "_"))
                        print("| TITLE".ljust(15, " ") + "|" + "VALUE".rjust(20, " ") + " |")
                        print(" ".ljust(15, "-") + " " + " ".rjust(22, "-"))
                        for k,v in i.items():
                            #if i["Transaction"] == type:
                                print(f"| {k}".ljust(15, " ") + "|" + f"{v}".rjust(20, " ") + " |")
                        print(" ".ljust(15, "-") + " " + " ".rjust(22, "-"))
                return
                break
            else:
                print("Wrong TRANSACTION type entered....TRY AGAIN")
                attempts += 1
        return "Too many failed attempts"




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
    

#Implementing a BANK to manage multiple accounts
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.owner} added to {self.name} Bank")

    def list_accounts(self):
        print(f"Accounts in {self.name}".center(50, "_"))
        for acc in self.accounts:
            print(f"- {acc.owner}")

    def find_account(self, owner_name):
        for acc in self.accounts:
            if acc.owner.lower() == owner_name.lower():
                return acc
        return None


            

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

print(acc_1.get_transactions_1())