'''
the attribute "address" belongs to the instance "data"
'''
class Employee:
    name="fahim"
    salary=25
    # it will get name becoz of class attributes
    # i have not given address directly but it will get it bacoz of instance attributes
    def printAddress(self):
        print(f"your name is {self.name} and address address is {self.address}")

data=Employee()
data.address="CTG"
print("salary",data.salary)
data.printAddress()