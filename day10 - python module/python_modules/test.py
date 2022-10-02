import myModule
# re-naming a module
import myModuleTwo as agePrinter
# You can choose to import only parts from a module, by using the from keyword.
from myModuleThree import person3


myModule.greeting("fahim")

print(myModule.person1["name"])

agePrinter.printAge(33)

print(person3["ageT"])