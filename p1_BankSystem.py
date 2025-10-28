from datetime import datetime
import string, random, csv, os

class BankAccount:
    def assign_balance(self):
        file_path = rf"{self.owner}_transactions.csv"

        check = os.path.exists(file_path)
        if not check:
            return 0
        else:
            with open(file_path, "r") as csv_file:
                content = csv.reader(csv_file)
                csv_list = []
                for row in content:
                    csv_list.append(row)
                
                balance = csv_list[-1][-1]
                balance = float(balance)
                return balance
        


    def __init__(self, owner):
        self.owner = owner
        self.__acc_no = 0
        self.__balance = self.assign_balance()
        self.__transactions = []
        self.__pin = 1
        self.__csv = [[" ", " ", self.owner, " ", " "],
                      ["Amount", "Time", "Transaction", "ID", "Balance"]]

    def trans_ID(self):
        return "TXN-" + ''.join(random.sample(string.ascii_letters + string.digits, 10))
    
    # putting transactions into a .csv file
    def _csv_write(self, info):

        file_path = rf"{self.owner}_transactions.csv"

        file_exists = os.path.exists(file_path)
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                for row in self.__csv:
                    writer.writerow(row)
   
            writer.writerow(info)
  
  

    def deposit(self, amount):
        print(f"{self.owner} DEPOSIT Management".center(50, "_"))
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
                    info = {"Transaction":"DEPOSIT",
                                            "ID":ID,
                                            "Amount":amount,
                                            "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}
                    # Storing the transaction details into the Transaction Log
                    self.__transactions.append(info)
                    info_list = [amount, info["Time"], "DEPOSIT", ID, self.__balance]

                    self._csv_write(info_list)

                    return f"""\nDeposited: {amount}
Transaction ID: {ID}"""
            elif depo == False:
                attempts += 1
            else:
                print(depo)
        
        return "Too many Failed attempts" 
    

    
    def withdraw(self, amount):
        print(f"{self.owner} WITHDRAWAL Management".center(50, "_"))
        attempts = 0

        # to limit number of PIN input attempts to 3
        while attempts < 3:
            w_draw = self._verify_pin(attempts)
            if w_draw == True:
                if amount <= 0:
                    return "Amount has to be greater than ZERO"
                else:
                    if amount > self.__balance:
                        return "\nYou have insufficient funds....."
                    else:
                        self.__balance -= amount
                        ID = self.trans_ID()
                        info = {"Transaction":"WITHDRAW",
                                                "ID":ID,
                                                "Amount":amount,
                                                "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}

                        # Storing the transaction details into the Transaction Log
                        self.__transactions.append(info)
                        info_list = [amount, info["Time"], "WITHDRAW", ID, self.__balance]

                        self._csv_write(info_list)
                        
                        return f"""\nWithdrawn: {amount}
    Transaction ID: {ID}"""
            elif w_draw == False:
                attempts += 1
            else:
                print(w_draw)

        return "Too many Failed attempts"
    
        
    def display_balance(self):
        print(f"{self.owner}'s Balance Display".center(50, "_"))
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
        print(f"{self.owner} TRANSACTION HISTORY".center(40, "_"))

        attempts = 0
        while attempts < 3:
            get_trans = self._verify_pin(attempts)
            if get_trans == True:

                type_attempts = 0
                while type_attempts < 3:
                    type = input("Choose transaction type ('WITHDRAW','DEPOSIT','INTEREST', 'FUNDS SENT' and 'FUNDS RECEIVED'): ")
                    type = type.upper()
                    types = ["WITHDRAW", "DEPOSIT", "FUNDS SENT", "FUNDS RECEIVED"]
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
                    else:
                        print("Wrong TRANSACTION type entered....TRY AGAIN")
                        type_attempts += 1
                    
                return "Too many failed attempts"
            elif get_trans == False:
                attempts += 1
            else:
                print(get_trans)

        return "Too many failed attempts"




    def change_pin(self):
        print(f"{self.owner} PIN CHANGE Management".center(50, "_"))
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
        
    # this for the 'BankAccount' sending the funds to record a Funds-Sent transaction.    
    def funds_transfer(self, bank_obj, account_obj):
        print(f"{self.owner} FUNDS TRANSFER Management".center(50, "_"))
        attempts = 0
        
        while attempts < 3:
            eft = self._verify_pin(attempts)
            if eft == True:
                if account_obj not in bank_obj._Bank__accounts:
                    return f"{account_obj.owner} has no account in {bank_obj.name}"
                else:
                    am_attempts = 0

                    while am_attempts < 3:
                        try:
                            transfer_am = int(input(f"How much do you want to transfer to {account_obj.owner}'s account: "))
                            if transfer_am > self.__balance:
                                am_attempts += 1
                                print("You have insufficient funds")
                            else:
                                self.__balance -= transfer_am
                                account_obj._BankAccount__balance += transfer_am
                                ID = self.trans_ID()
                                info = {"Transaction":"FUNDS SENT",
                                                        "ID":ID,
                                                        "Amount":transfer_am,
                                                        "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}
                                
                                # Storing the transaction details into the Transaction Log
                                self.__transactions.append(info)
                                info_list = [transfer_am, info["Time"], "FUNDS SENT", ID, self.__balance]

                                self._csv_write(info_list)

                                account_obj._accept_fund(transfer_am, ID)

                                return f"Amount of {transfer_am} succefully transferred to {account_obj.owner}"
                            
                        except ValueError:
                            print("TRANSFER amount has to be an integer")

                    return "Too many failed attempts (a)"

            elif eft == False:
                attempts += 1
            else:
                print(eft)

        return "Too many Failed attempts (p)"
    
    # this for the 'BankAccount' receiving the funds to record a Funds-Received transaction.
    def _accept_fund(self, received, f_ID):
        info = {"Transaction":"FUNDS RECEIVED",
                                "ID":f_ID,
                                "Amount":received,
                                "Time":datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}
        
        # Storing the transaction details into the Transaction Log
        self.__transactions.append(info)
        info_list = [received, info["Time"], "FUNDS RECEIVED", f_ID, self.__balance]

        self._csv_write(info_list)
        


        
class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def apply_interest(self):
        interest = self._BankAccount__balance * SavingsAccount.interest_rate
        self._BankAccount__balance += interest
        print(f"Interest of {interest} applied at rate {SavingsAccount.interest_rate * 100}%")
        ID= self.trans_ID()
        info = {"Transaction":"Interest",
                     "ID": ID,
                     "Amount": interest,
                     "Time": datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}
        self._BankAccount__transactions.append(info)
        info_list = [interest, info["Time"], "INTEREST", ID, self._BankAccount__balance]

        self._csv_write(info_list)

    

#Implementing a BANK to manage multiple accounts
class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []
        self.__acc_nos = []

    # adds the "given" BankAccount object to the self.__accounts list of the current Bank instance
    def add_account(self, account_obj):
        if account_obj in self.__accounts:
            print(f"Account Provided is already registered in {self.name}")
        else:
            self.__accounts.append(account_obj)
            self._acc_no_gen(account_obj)
            print(f"Account successfully added to {self.name} ")

    # removes the "given" BankAccount object from the self.__accounts list of the current Bank instance
    def remove_account(self, account_obj):
        if account_obj not in self.__accounts:
            print(f"Account Provided is not registered in {self.name}")
        else:
            self.__accounts.remove(account_obj)
            self.__acc_nos.remove({account_obj._BankAccount__acc_no : account_obj.owner})
            print(f"Account successfully removed from {self.name}")

    # returns all the BankAccount owner names registered in the current "Bank" instance
    def list_accounts(self):
        print(f"{self.name} Account Database".center(40,"_"))
        print(" ".ljust(20, "-") + " " + " ".rjust(22, "-"))
        print("| ACCOUNT OWNER".ljust(20, " ") + "|" + "ACCOUNT NUMBER".rjust(20, " ") + " |")
        print(" ".ljust(20, "-") + " " + " ".rjust(22, "-"))
        for i in self.__acc_nos:
            for k, v in i.items():
                print(f"| {k}".ljust(20, " ") + "|" + f"{v}".rjust(20, " ") + " |")
        print(" ".ljust(20, "-") + " " + " ".rjust(22, "-"))

    # checks the availability of a 'given' owner's BankAccount in the record of registered BankAccounts to the current Bank instance
    def find_account(self, owner_name):
        for acc in self.__accounts:
            if acc.owner.lower() == owner_name.lower():
                return f"Account for {owner_name} is registered in {self.name}"
        return f"Account for {owner_name} is not registered in {self.name}"
    
    def _acc_no_gen(self, account_obj):
        while True:
            acc_no = random.randint(1000000000,9999999999)

            if {acc_no : account_obj.owner} in self.__acc_nos:
                continue
            else:
                self.__acc_nos.append({acc_no : account_obj.owner})
                account_obj._BankAccount__acc_no = acc_no
                break

    def interest_to_all(self):
        for account in self.__accounts:
            account.apply_interest()

            