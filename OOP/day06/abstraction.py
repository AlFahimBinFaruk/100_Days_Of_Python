from abc import ABC, abstractclassmethod


class ClassOne(ABC):
    @abstractclassmethod
    def myABS(self):
        pass


class ClassTwo(ClassOne):
    def myABS(self):
        print("This is an abstracted class")


obj = ClassTwo()
obj.myABS()
