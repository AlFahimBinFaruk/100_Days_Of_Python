class MyClass:
    __name = "fahim"
    __age = 33;

    def getter(self):
        return f"name is {self.__name} and age is {self.__age}"

    def setter(self, name, age):
        self.__name = name
        self.__age = age


obj = MyClass()
print(obj.getter())

# obj.name="Suhan"
# obj.age=55
obj.setter("suhan",44)

print(obj.getter())
