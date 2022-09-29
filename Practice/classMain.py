""" Python does not support Constructor overloading """

# class MyClass:
#     name = "Fahim"
#
#     def __init__(self):
#         print("Calling First")

    # def printAge(self):
    #     print("age is", self.age)


# obj=MyClass("fahim")
# print(obj.name)
#
# obj.age=33
# obj.printAge()

# objTwo = MyClass()

# class ClassTwo:
#     def __init__(self):
#         print("calling")
#
#     def myFunc(self):
#         print("ok",self.name)
#
#     @staticmethod
#     def staticFunc(name,age):
#         print("name",name,"age",age)

    # @classmethod
    # def classFunc(x,y):
    #     print("name", x, "age", y)

# obj=ClassTwo()
#
# obj.name="Suhan"
# obj.myFunc()
#
# obj.staticFunc("fahim",44)

# class method is not clear yet

# ClassTwo.classFunc(44,55)

# class ClassOne:
#     name="fahim"
#     age=33
#
#     def printCOne(self):
#         print("Name is ",self.name,"age is",self.age)
#
# 
# class ClassTwo(ClassOne):
#     gender="Male"
#     address="BD"
#
#     def printCTwo(self):
#         print("address is",self.address,"gender is ",self.gender)
#
#
# obj= ClassTwo()
#
# obj.printCTwo()
# obj.printCOne()