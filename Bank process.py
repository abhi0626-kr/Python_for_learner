
# # Create a Bank process using OOPS concept in Python:

# class BankAccount:
    
#     def __init__(self,Name, balance):
#         self.Name = Name
#         self.balance = balance
#         print(f"Hi {self.Name}, Your Account Created Successfully")
        
#     def display_balance(self):
#         print(f"Hi {self.Name}, Your Account Balance is {self.balance}")        
        
#     def deposit(self,amount):
#         if amount >=100:
#             self.balance += amount # self.balance = self.balance + amount
#             print(f"Hi {self.Name}, Amount Depostied Sucessfully")
#             print(f"Updated Balance: {self.balance}")
#         else:
#             print("Deposit Amount Failed")
#             print("You Deposit Amount Should be Minimum 100 Rs")
            
#     def withdraw(self, amount):
#         if amount >self.balance or amount <100:
#             print("Withdrew Amount Failed")
#             print("You Withdrew Amount Should be Less than Your Account Balance or cannot accept less than 100 Rs")
#         else:    
#             self.balance -= amount # self.balance = self.balance - amount
#             print(f"Hi {self.Name}, Amount Withdrawn Sucessfully")
#             print(f"Updated Balance: {self.balance}")
# User1 = BankAccount('Alex',5000)
# User1.display_balance()
# User1.deposit(10000)
# User1.withdraw(2000)
# User1.withdraw(876)
# User1.withdraw(898776)
# New_user = BankAccount("David",9000)
# New_user.withdraw(1000)
# New_user.balance
# #------------------------------------------------------------------------------------------------------------




import json
import os

account={}
fileName = 'AccountDetails.json'

def load_json(fileName):
    if os.path.exists(fileName):
        with open(fileName,'r') as file:
            return json.load(file)
    else:
        return {}

def load_data_toMemory(fileName):

    acc_dt = load_json(fileName)

    for AccNo, acc_values in acc_dt.items():
        if acc_values.get("AccType")=='Savings':
            account[AccNo] = SavingsAccount(acc_values["UserName"], acc_values["Balance"])
        elif acc_values.get("AccType")=='Current':
            account[AccNo] = CurrentAccount(acc_values["UserName"], acc_values["Balance"])
   



def save_json():
    data={}

    for AccNo, acc_items in account.items():

        if 'S' in AccNo:
            AccType ='Savings'
        elif 'C' in AccNo:
            AccType='Current'
        else:
            AccType= 'UNKNOWN'
        print(acc_items._balance)

        data[AccNo] ={'UserName' :acc_items.username,
                      'AccType':AccType,
                      'Balance':acc_items._balance}

        with open(fileName,'w') as file:
            json.dump(data,file,indent= 2)

class Account:
    def __init__(self, username, balance=0):
        self.username = username
        self._balance = balance

    def deposit(self, amount):
        if amount <100:
            print(f'Hi {self.username} , Deposit amount should be greater than 99')
        else:
            self._balance += amount # self._balance = self._balance + amount
            print(f"Hi {self.username} ,Amount Deposited Successfully")
            print(f"Deposited Amount: {amount}")
            print(f"Updated Balance:{self._balance}")
#             save_json()
    
    def withdraw(self, amount):
        if amount > self._balance or amount <100:
            print(f"Hi {self.username}, Amount withdraw is failed")
            print(f'You are trying to withdraw {amount}Rs, but your current balance is {self._balance}')
        else:
            self._balance -= amount # self.balance = self.balance - amount 
            print(f"Hi {self.username} ,Amount Withdrawn Successfully")
            print(f"Withdrawn Amount: {amount}")
            print(f"Updated Balance:{self._balance}")
            save_json()
            
    def display_balance(self):
        return f"Hi {self.username} , Total Balance in your account {self._balance} Rs"

    class SavingsAccount(Account):
    
        def add_intrest(self, intrestRate=(1/100)):
            if self._balance >=50000:
                if intrestRate<=(3/100):
                    intrestRate=3/100 
                else:
                    intrestRate= intrestRate

            else:
                if intrestRate<=(1/100):
                    intrestRate= (1/100)
                else:
                    intrestRate= intrestRate

            IntrestCalc = self._balance *intrestRate
            self._balance += IntrestCalc
       
            print(f'Hi {self.username}, Interest Given by bank is {intrestRate}')
            print(f"Intrest Credited To Your Account is {IntrestCalc}")
            print("Updated Balance:",self._balance)
            save_json()
            return self._balance


class CurrentAccount(Account):
    def add_intrest(self, intrestRate=(3/100)):
        if self._balance >=150000:
            if intrestRate<=(6/100):
                intrestRate=6/100 
            else:
                intrestRate= intrestRate

        else:
            if intrestRate<=(3/100):
                intrestRate= (3/100)
            else:
                intrestRate= intrestRate

        IntrestCalc = self._balance *intrestRate
        self._balance += IntrestCalc
        print(f'Hi {self.username}, Interest Given by bank is {intrestRate}')
        print(f"Intrest Credited To Your Account is {IntrestCalc}")
        print("Updated Balance:",self._balance)
        save_json()
        return self._balance
            

def Account_Creation(UserName, AccountType):

    if Account_Type == 1:
        AccountType= 'Savings'
        AccNo= 100
        while 'S'+str(AccNo) in account:
            AccNo+=1
            continue
        else:
            Updated_AccNo= 'S'+str(AccNo)
            print(Updated_AccNo)
            balance= int(input("Enter Your Balance for intial Deposit: "))
            if balance <=0:
                balance=0
                print("""You have entered the balance which is not met our bank Policy,
                So We created ZeroBalance Account So that You can deposit the amount later also""")

            account[Updated_AccNo]= SavingsAccount(UserName,balance)
            print(f"Hi {UserName}, Your {AccountType} Account is Created and Your Account Number is {Updated_AccNo}")
            save_json()

    elif Account_Type == 2:
        AccountType= 'Current'
        AccNo= 100
        while 'C'+str(AccNo) in account:
            AccNo+=1
            continue
        else:
            Updated_AccNo= 'C'+str(AccNo)
            balance= int(input("Enter Your Balance for intial Deposit: "))
            if balance <10000:
                print(f"Hi {UserName} you are opening a current Account, You minimum deposit should 10000")
                print('Sorry Your Account is not created')
            else:
                account[Updated_AccNo]= CurrentAccount(UserName,balance)
                print(f"Hi {UserName}, Your {AccountType} Account is Created and Your Account Number is {Updated_AccNo}")
                save_json()
                
    else:
        print("No Other Options is Left. Kindly Contact the Bank")


def operations():
    
    operations= int(input("Enter the Service You want to avali\n 1. Deposit\n 2. WithDrawn\n 3. Display_Balance"))
    AccNo= input("Enter your Account Number: ")
    
    if AccNo in account:
        if operations==1:
            Deposit_Amt= int(input("Enter the Amount to deposit: "))
            print(account[AccNo].deposit(Deposit_Amt))

        elif operations ==2:
            withdraw_Amt = int(input("Enter the Amount to Withdraw: "))
            print(account[AccNo].withdraw(withdraw_Amt))

        elif operations==3:
            print(account[AccNo].display_balance())
        else:
            print("Enter the Correct Input")

    else:
        print("Sorry The given Account Number is Not valid. Enter the Correct Account Number")


load_data_toMemory(fileName)

while True:
    try:
        Question = int(input("""Choose the Option\n 1. Account Creation\n 2. Operation(Deposit, Withdrawn, Check Balance) \n 3. Exit """))
    except ValueError:
        print("Kindly enter the Correct Values")
        continue
    else:
        if Question==1:
            try:
                UserName= input("Enter the Name: ")
                Account_Type= int(input("""Enter the Account Type \n 1 - Savings Account \n 2 - Current Account\n"""))
            except ValueError:
                print("Kindly Enter the Numeric Values for Account_Type")
            else:
                try:
                    Account_Creation(UserName,Account_Type)  
                    confirmation= input("Wheather You need to Continue to Deposit, Withdrawn or Check balance - (Yes/No)")

                    if confirmation.lower()=='yes':
                        operations()
                        continue
                    elif confirmation.lower()=='no':
                        print("ThankYou for Banking with us...")
                        break  
                    
                except ValueError:
                    print("Kindly enter the Correct Values")
                    continue
        elif Question ==2:    
            try:
                operations()
                continue
            except ValueError:
                print("Kindly enter the Correct Values")
                continue
                
        elif Question==3:
            print("ThankYou for Banking with us...")
            break
            