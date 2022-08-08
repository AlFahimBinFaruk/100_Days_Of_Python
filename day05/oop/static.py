'''
1.by default the functions inside class takes "self" as first "argument".
2.but inside "@staticmethod" it will act as an "normal function"(will not take self as first arg.)
'''


class Employee:
    name = "fahim"

    def printAddress(self, address):
        print(f"your name is {self.name} and address address is {address}")

    @staticmethod
    def greet(user):
        print(f"Hi {user}")


data = Employee()
data.printAddress("Dhaka")
data.greet("suhan")