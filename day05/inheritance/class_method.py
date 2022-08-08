'''
When we change any attribute the original attribute doesnt change only the instance of it change to solve this problem we will use
1.__class__
2.@classmethod
'''
# original salary will remain 33 only instance of salary will change
'''
class Employe:
    name="Fahim"
    salary=33
    def changeSalary(self):
        self.salary=55
'''

# solution 01
'''
class Employe:
    name="Fahim"
    salary=33
    def changeSalary(self):
        self.__class__.salary=55
'''
# solution 02
class Employe:
    name="Fahim"
    salary=33
    @classmethod
    def changeSalary(cls):
        cls.salary=55


data=Employe()
print("instance data=>",data.salary)
data.changeSalary()
print("instance data=>",data.salary)
print("class data=>",Employe.salary)