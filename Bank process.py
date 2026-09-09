
# Create a Bank process using OOPS concept in Python:

class BankAccount:
    
    def __init__(self,Name, balance):
        self.Name = Name
        self.balance = balance
        print(f"Hi {self.Name}, Your Account Created Successfully")
        
    def display_balance(self):
        print(f"Hi {self.Name}, Your Account Balance is {self.balance}")        
        
    def deposit(self,amount):
        if amount >=100:
            self.balance += amount # self.balance = self.balance + amount
            print(f"Hi {self.Name}, Amount Depostied Sucessfully")
            print(f"Updated Balance: {self.balance}")
        else:
            print("Deposit Amount Failed")
            print("You Deposit Amount Should be Minimum 100 Rs")
            
    def withdraw(self, amount):
        if amount >self.balance or amount <100:
            print("Withdrew Amount Failed")
            print("You Withdrew Amount Should be Less than Your Account Balance or cannot accept less than 100 Rs")
        else:    
            self.balance -= amount # self.balance = self.balance - amount
            print(f"Hi {self.Name}, Amount Withdrawn Sucessfully")
            print(f"Updated Balance: {self.balance}")
User1 = BankAccount('Alex',5000)
User1.display_balance()
User1.deposit(10000)
User1.withdraw(2000)
User1.withdraw(876)
User1.withdraw(898776)
New_user = BankAccount("David",9000)
New_user.withdraw(1000)
New_user.balance
#------------------------------------------------------------------------------------------------------------
class BankAccount1:
    
    def __init__(self,Name, balance):
        self.Name = Name
        self.__balance = balance
        print(f"Hi {self.Name}, Your Account Created Successfully")
        
    def display_balance(self):
        print(f"Hi {self.Name}, Your Account Balance is {self.__balance}")        
        
    def __deposit(self,amount):
        if amount >=100:
            self.__balance += amount # self.balance = self.balance + amount
            print(f"Hi {self.Name}, Amount Depostied Sucessfully")
            print(f"Updated Balance: {self.__balance}")
        else:
            print("Deposit Amount Failed")
            print("You Deposit Amount Should be Minimum 100 Rs")
            
    def withdraw(self, amount):
        if amount >self.__balance or amount <100:
            print("Withdrew Amount Failed")
            print("You Withdrew Amount Should be Less than Your Account Balance or cannot accept less than 100 Rs")
        else:    
            self.__balance -= amount # self.balance = self.balance - amount
            print(f"Hi {self.Name}, Amount Withdrawn Sucessfully")
            print(f"Updated Balance: {self.__balance}")
David = BankAccount1('David',90000)
David.__balance
David.display_balance()