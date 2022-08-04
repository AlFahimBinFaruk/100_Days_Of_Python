'''
Set is a collection of non repetetive items in Python.
set will ignore items that are repeated.
sets are more like list..
'''
''' 
you cannot add 
1.list 
2.dictionary
inside a set
'''
'''
set'a are 
1.unordered
2.unindexed
3.there is no way  to change items in set
'''

# any mutable data type cannot be stored inside set

mySet = {"zayn", 2, 3, 4, 5, "Suhan", False}
print(mySet)
'''How to create an empty set'''
# this will create an empty dictionary not set
x = {}
print(type(x))

# this will create an empty set
a = set()
print(type(a))
'''Add items in set'''
setTwo = set()
setTwo.add("fahim")
setTwo.add(33)
print(setTwo)
'''Methods of set'''

# get the lenght of set
print("Length is=>", len(mySet))

# remove items from set by value
mySet.remove(False)
print(mySet)

# removes a random value from a set
mySet.pop()
print(mySet)

'''Union and Intersections are like the set math of class 10'''
'''Union of set'''
testOne = {1, 2, 3, 4, 56, 5}
testTwo = {1, 4, 3, 2, 4, 5}

print("Union", testOne.union(testTwo))

'''Intersection of set'''
print("Intersection", testOne.intersection(testTwo))


testThree={4,4.0,4.1,4.4,4.9,5}
print(len(testThree))