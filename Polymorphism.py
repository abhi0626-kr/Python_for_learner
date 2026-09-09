# Polymorphism

# Method Overriding

class ABCD_Technologies:
    def employees(self):
        print("ABC Technolgies Employees are being called")
        
        
class Google_0(ABCD_Technologies):
    def employees(self):
        print("Google Employees are Being Called")

Project = Google_0()
Project.employees()



# SuperClass
# SuperClass Means Parent Class

# super().funcName()
class ABC_Technologies:
    def employees(self):
        print("ABC Technolgies Employees are being called")
        
        
class Google(ABC_Technologies):
    def employees(self):
        print("Google Employees are Being Called")
        super().employees()

prj= Google()
prj.employees()