# class MyClass:
#     salary=33

    # def changesalary(self):
    #     self.salary=44

    # sol 01
    # def changesalary(self):
    #     self.__class__.salary=44

    # sol 02
    # @classmethod
    # def changesalary(cls):
    #     cls.salary=44

# obj=MyClass()
# print("obj",obj.salary)
# print("class",MyClass.salary)
# obj.changesalary()
#
# print("obj",obj.salary)
# print("class",MyClass.salary)

# class Employe:
#     salary = 33
#     bonus = 3
#
#     # property or getter means look like function but act like property
#     @property
#     def totalSalary(self):
#         return (self.bonus + self.salary)
#
#     # setter
#     # in here we are changing bonus to match will the new salary
#     @totalSalary.setter
#     def totalSalary(self, newSalary):
#         self.bonus = newSalary - self.salary
#
#
# data = Employe()
# print("salary",data.salary)
# print(data.totalSalary)
# data.totalSalary = 333
# print(data.bonus)

# class COne:
#     def printCOne(self):
#         print("calling c one")
#
#     def common(self):
#             print("calling c one common")
#
# class CTwo:
#     def printCTwo(self):
#         print("calling c two")
#
#     def common(self):
#         print("calling c two common")
#
# class Test(CTwo,COne):
#     def printTest(self):
#         print("calling test")
#
# obj=Test()
# obj.printCOne()
# obj.printCTwo()
# obj.printTest()

# if a function with same name exits in both class it will call the function of that class which is inherited first (CTwo)
# obj.common()


'''
__add__,__mul__ are dunder methods that are built in and used for operator overloading.
'''

# class Number:
    # num=33

    # def __init__(self, num):
    #     self.num = num
    #
    # def __add__(self, num2):
    #     return self.num + num2.num
    #
    # def __mul__(self, num2):
    #     return self.num * num2.num
    #
    # def __str__(self):
    #     return f"num is {self.num}"


# dataOne = Number(5)
# dataTwo = Number(5)

# this will call __str__
# print("one",dataOne,"two",dataTwo)

# this will call __add__
# print(dataOne+dataTwo)

# this will call __mul__
# print(dataOne*dataTwo)

# if both "attributes name are same" but we want to call the "attribute of inherited class" then we will use "super()"
# class Employe:
#
#     def greet(self):
#         print("This is employee greet!!")
#
#
# class Language(Employe):
#
#     def greet(self):
#         print("This is language greet!!")
#         super().greet()
#         # it will go to infinite loop
#         #self.greet()
#
#
# data = Employe()
# dataTwo = Language()
# dataTwo.greet()