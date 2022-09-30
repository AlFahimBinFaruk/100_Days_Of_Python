'''
__add__,__mul__ are dunder methods that are built in and used for operator overloading.
'''


class Number:

    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num

    def __mul__(self, num2):
        return self.num * num2.num


dataOne = Number(3)
dataTwo = Number(4)
sum = dataOne + dataTwo
mul = dataOne * dataTwo
print(sum)
print(mul)