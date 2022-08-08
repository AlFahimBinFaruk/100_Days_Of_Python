# if both "attributes name are same" but we want to call the "attribute of inherited class" then we will use "super()"
class Employe:

    def greet(self):
        print("This is employee greet!!")


class Language(Employe):

    def greet(self):
        print("This is language greet!!")
        super().greet()
        # it will go to infinite loop
        #self.greet()


data = Employe()
dataTwo = Language()
dataTwo.greet()