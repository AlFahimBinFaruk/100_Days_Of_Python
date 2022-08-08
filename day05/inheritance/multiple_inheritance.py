class Mom:
    momName = "Fahim's mom"

    def hiMom(self):
        print("Hi Mom")


class Dad:

    def hiDad(self):
        print("Hi Dad")


# Multiple inheritance = one class can inherit multiple class
class Child(Mom, Dad):

    def greet(self):
        print(f"I am Fahim my mom is {self.momName}")
        self.hiMom()


momIn = Mom()
dadIn = Dad()
childIn = Child()
childIn.hiDad()
childIn.greet()