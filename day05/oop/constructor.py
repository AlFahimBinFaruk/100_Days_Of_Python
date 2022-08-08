'''
1.the __init__(self) by default call itsef when the class is initialized
'''
# normal syntax
class Employee:
    def __init__(self):
        print("I am running auto!!")

data=Employee()

# with arguments
class EmployeeTwo:
    def __init__(self,name,country):
        print(f"hello {name} from {country}")
dataTwo=EmployeeTwo("fahim","BD")

# name and salary will be given when we initialize the class
class EmployeeInfo:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getDetails(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")

dataThree=EmployeeInfo("Suhan",333)
dataThree.getDetails()