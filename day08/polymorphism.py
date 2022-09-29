""" Polymorphism with a Function and objects """
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
#
#
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")
#
#
#
#
#
# bird = Bird()
# spr = sparrow()
#
#
# bird.intro()
# bird.flight()
#
# spr.intro()
# spr.flight()


""" polymorphism with class method """
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

