'''
There are two types of functions in python
1.Built in = sum(),int(),list()
2.User defined
'''
# syntax
def printName(name):
     print(f"Hi {name}")

# calling function
printName("fahim")
printName("suhan")

# return in function
def averageMark(markList):
    avg=(sum(markList)/len(markList))*100
    return avg

myAvg=averageMark([4,5,6,6,7])
print("My avg =>",myAvg)

fahimsAvg=averageMark([45,56,63,64,73])
print("Fahims avg =>",fahimsAvg)

# functions with multiple arguments
def greetUser(name,age,location):
    print(f"welcome {name} of age {age} in {location}")

greetUser("fahim",33,"CTG")

# default arguments in a functions
def sayHI(name="User"):
    print(f"Helllo {name}")

sayHI("suhan")