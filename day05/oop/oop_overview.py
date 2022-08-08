'''Normal way/ procedural programming'''
a = 12
b = 10
print("Sum =>", a + b)


'''OOP Way'''
'''
1.the first word of classname will be capital.
2.self mean the instance of class
in here self means the instance "num" of class "Number"
'''
class Number:

    def sum(self):
        return self.x + self.y


num = Number()
num.x = 33
num.y = 45
sum = num.sum()
print("OOP Sum =>", sum)
