class Employe:
    salary=33
    bonus=3
    
    # property or getter means look like function but act like property
    @property
    def totalSalary(self):
        return (self.bonus+self.salary)
    # setter
    # in here we are changing bonus to match will the new salary
    @totalSalary.setter
    def totalSalary(self,newSalary):
        self.bonus=newSalary-self.salary
    

data=Employe()
print(data.totalSalary)
data.totalSalary=333
print(data.bonus)