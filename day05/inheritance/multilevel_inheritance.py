class Person:
    name="Fahim"
    country="BD"

class Employee(Person):
    company="Honda"

class Profile(Employee):
    job="Backend Dev"

personIn=Person()
employeIn=Employee()
profileIn=Profile()
print(profileIn.name)
print(profileIn.company)
print(employeIn.country)