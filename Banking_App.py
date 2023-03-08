'''

                             #====== Banking App ======#

This app allows a user with a recognised username and password to login to their bank account.
They are able to see their balance sheet, withdraw or deposit money - this information is stored in 
external files. The programme consists of: (1) the Bank class containing various methods (2) username
and password check that runs a user entery passed "user.txt" and (3) an options menu that calls on the 
methods in the Bank class.

'''

import os
from datetime import date

#----Classes and Definitions----#

class Bank:
    
    def date_now(self):
        
        current_date = date.today()
        f_date = f"{current_date.day} {date.today().strftime('%b')} {current_date.year}"
        
        return f_date
    
    def return_balance(self):
        
        with open("balance.txt", "r") as balance:
            lines = balance.readlines()
            list_lines = []
            
            for line in lines:
                list_lines.append(line)
            
            return list_lines[-1]
        
        balance.close()
    
    def read_bank_account(self):
    
        with open("bank_account.txt", "r") as bank:
            lines = bank.readlines()
            for line in lines:
                print(f"{line}")
        
        print(f"\nYour balance is £{self.return_balance()}")
        
        bank.close()
                      
    def withdraw(self, user_withdraw):
        
        with open("bank_account.txt", "a+") as bank:
            
            d = Bank.date_now(self)
            
            bank.write(f"{d}: withdrawl: £{user_withdraw}\n")
            
        bank.close()
        
        with open("balance.txt", "r") as balance, open("temp.txt", "a+") as temp:
            
            b = balance.readlines()
            
            bal = b[0]
            
            bal = int(bal)
            bal = bal - user_withdraw
            
            bal = str(bal)
            
            temp.write(bal)
            os.remove("balance.txt")
            os.rename("temp.txt", "balance.txt")
            
            balance.close()
            temp.close()
            
        
        print(f"You have withdrawn £{user_withdraw}")
        
        print(f"Your new balance is £{self.return_balance()}")
    
    def deposit(self, user_deposit):
        
        with open("bank_account.txt", "a+") as bank:
            
            d = Bank.date_now(self)
            
            bank.write(f"{d}: deposit: £{user_deposit}\n")
            
        bank.close()
        
        with open("balance.txt", "r") as balance, open("temp.txt", "a+") as temp:
            
            b = balance.readlines()
            
            bal = b[0]
            
            bal = int(bal)
            
            bal = bal + user_deposit
            
            bal = str(bal)
            
            temp.write(bal)
            os.remove("balance.txt")
            os.rename("temp.txt", "balance.txt")
            
            balance.close()
            temp.close()
            
        
        print(f"You have deposited £{user_deposit}")
        
        print(f"Your new balance is £{self.return_balance()}")

bank = Bank()

#------Username and Password Check------#

f = open("user.txt", "r")

authenticated = False

lines = f.readlines()

while authenticated == False:
    
    user_name = input("Please enter your username: ")
    user_name = user_name.lower()
    user_password = input("Please enter your password: ")
    user_password = user_password.lower()
    
    for line in lines:
        line = line.strip("\n").split(", ")
        
        if user_name == line[0] and user_password == line[1]:
            authenticated = True
        else:
            continue

    if authenticated == True:
        print("\nYou're through to your bank account.\n")
    else:
        print("\nSorry that username and password are not accepted! Try again.\n")
            
f.close()
        
#------Interactive Banking App------#

while True:
    
    user_option = input('''Please select from the following menu:
(1) to show balance sheet
(2) to withdraw money
(3) to deposit money
(4) exit
:''')

    if user_option == "1":
        
        bank.read_bank_account()
        
    elif user_option == "2":
        
        user_withdraw = input("How much would you like to withdraw (in £)?:")
        user_withdraw = int(user_withdraw)
        
        bank.withdraw(user_withdraw)
        
    elif user_option == "3":
        
        user_deposit = input("How much would you like to deposit (in £)?:")
        user_deposit = int(user_deposit)
        
        bank.deposit(user_deposit)
        
    elif user_option == "4":
        
        break
        print("Logging out")     
        
    else:
        continue
