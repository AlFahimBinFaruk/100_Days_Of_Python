class MyClass:
    __name = "fahim"
    __age = 33
    _ran=33

    def getter(self):
        return f"name is {self.__name} and age is {self.__age}"

    def setter(self, name, age):
        self.__name = name
        self.__age = age


obj = MyClass()
print(obj.getter())

obj.setter("suhan",44)

print(obj.getter())

# this can be accessed
print(obj._ran)

# this will give error as __ means private attribute that can only be accssed inside the same class
# print(obj.__name)

"""The Python interpreter modifies the variable name with ___. 
So Multiple times It uses as a Private member because another class can not access that variable directly. 
The main purpose for __ is to use variable /method in class only If you want to use it outside of the class 
you can make it public."""
