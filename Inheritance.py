# Inheritance
    # Inheritance is 
    # Inheritance is a mechanism in which one class acquires the properties and methods of another class.

# Types of Inheritance:
    # Single
    # Multilevel
    # Hierarichal
    # Multiple
    # Hybrid

# Single Inheritance:
    # In single inheritance, a child class inherits from a single parent class.
class a: # Parent Class
    def display(self):
        print("Clas A Function is Called")

class b(a): # Child Class
    def display(self):
        # If the Two classes names are same then we can use super() to call the parent class function.
        super().display() 
        print("Clas B Function is Called")

# Creating an object of class B
obj = b()
obj.display() # Calling function from parent class


# Overriding Conpcets in Inheritance:

#Single Inheritance with Overriding:
class Employee_detail: # Parent Class
    def __init__(self, Emp_ID, Emp_Name, position):
        self.Emp_ID = Emp_ID
        self.Emp_Name = Emp_Name
        self.position = position

    def display_info(self):
        print(f"Emp_ID: {self.Emp_ID}, Emp_Name: {self.Emp_Name}, Position: {self.position}")

class Manager_detail(Employee_detail): # Child Class
    def __init__(self,Manager_ID,Manager_Name ,department,Emp_ID, Emp_Name, position):
        super().__init__(Emp_ID, Emp_Name, position)
        self.Manager_ID = Manager_ID
        self.Manager_Name = Manager_Name
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Manager ID: {self.Manager_ID}, Manager Name: {self.Manager_Name}, Department: {self.department}")
        

hr = Manager_detail("MGR001", "Sukuna", "Evil_Devil","EMP001", "Toji", "Assisnator")
hr.display_info()


# Mulitlevel Inheritance : 

class A: # Parent Class
    def display_A(self):
        print("Class A Function is Called")
class B(A): # Child Class
    def display_B(self):
        print("Class B Function is Called")

class C(B): # Child Class
    def display_C(self):
        print("Class C Function is Called")

obj = C() # We calling the class C object because
obj.display_A() # Calling function from parent class A
obj.display_B() # Calling function from parent class B
obj.display_C() # Calling function from class C



# Overriding Conpcets in Inheritance:

#Muilt Level Inheritance with Overriding:
class Employee_Info: # Parent Class
    def __init__(self, Emp_ID, Emp_Name, position):
        self.Emp_ID = Emp_ID
        self.Emp_Name = Emp_Name
        self.position = position

    def Employee_info(self):
        print(f"Emp_ID: {self.Emp_ID}, Emp_Name: {self.Emp_Name}, Position: {self.position}")

class Manager(Employee_Info): # Child Class
    def __init__(self,Manager_ID,Manager_Name ,department,Emp_ID, Emp_Name, position):
        super().__init__(Emp_ID, Emp_Name, position)
        self.Manager_ID = Manager_ID
        self.Manager_Name = Manager_Name
        self.department = department

    def Manager_info(self):
        super().Employee_info()
        print(f"Manager ID: {self.Manager_ID}, Manager Name: {self.Manager_Name}, Department: {self.department}")
        
class HR_Manager(Manager): # Child Class
    def __init__(self,HR_ID,HR_Name ,location,Manager_ID,Manager_Name ,department,Emp_ID, Emp_Name, position):
        super().__init__(Manager_ID,Manager_Name ,department,Emp_ID, Emp_Name, position)
        self.HR_ID = HR_ID
        self.HR_Name = HR_Name
        self.location = location

    def HR_info(self):
        super().Manager_info()
        print(f"HR ID: {self.HR_ID}, HR Name: {self.HR_Name}, Location: {self.location}")
        
obj = HR_Manager("HR001", "Maki", "Tokyo","MGR001", "Sukuna", "Evil_Devil","EMP001", "Toji", "Assisnator")
obj.HR_info()
obj.Employee_info()  # Calling function from parent class Employee_Info
obj.Manager_info()  # Calling function from parent class Manager





class Teacher:
    def __init__(self, T_ID, T_name, subject):
        self.T_ID = T_ID
        self.T_name = T_name
        self.subject = subject

    def Teacher_details(self):
        print(f"Teacher ID: {self.T_ID}, Teacher Name: {self.T_name}, Subject: {self.subject}")

    def student_details(self, S_ID, S_name, S_grade):
        print(f"Student ID: {S_ID}, Student Name: {S_name}, Student Grade: {S_grade}")

    def Pricriple(self, P_ID, P_name, P_location):
        print(f"Pricriple ID: {P_ID}, Pricriple Name: {P_name}, Pricriple Location: {P_location}")
obj = Teacher("T001", "Gojo", "Maths")
obj.Teacher_details()
obj.student_details("S001", "Itadori", "A")
obj.Pricriple("P001", "Sukuna", "Tokyo")