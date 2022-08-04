'''
Tuples and list are same 
the main differance is you cannot change the value of tuples.
Tuples are immutable..
'''

tOne=("fahim",3,4,False)
print(tOne)
print(tOne[3])
# empty tuple
tTwo=()
print(tTwo,type(tTwo))
# tuple with one element
tThree=(2,)
print(tThree)

'''Methods in Tuples'''
tFour=(3,4,4,6,6,3,5,6,"suhan")
'''count'''
# count how many 3 there are in tFour
print(tFour.count(3))
print(tOne.count("fahim"))
# know the index number of a tuple
print(tFour.index("suhan"))
print(tFour.index(3))