# Basic Concept with syntax of Inheritance
# Employe can't use Language class methods
# if same function or attrubutes exits in both classes then it will take its own function or attributes
class Employe:
    name="fahim"
    def printName(self):
        print(f"Hello {self.name}")
    def greet(self):
        print("This is employee greet!!")

# Language can use Employe class methods
# single inheritance
class Language(Employe):
    language="Python"
    def printLan(self):
        print(f"Work language is {self.language}")
    def greet(self):
        print("This is language greet!!")

eData=Employe()
lData=Language()
lData.printName()
lData.greet()
eData.greet()