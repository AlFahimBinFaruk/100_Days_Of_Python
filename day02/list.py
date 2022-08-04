'''
list are a collection of data in python
'''
nameList = ["fahim", 33, True, 23424, 43, 44, 43, 2, 2]

# change value of a list
nameList[1] = 23
print(nameList[1])

# list slicing
print(nameList[0:2])

# third arg mean skip
print(nameList[0:6:2])
'''sorting list '''
# sort() will change the original lOne and sort it in increasing order
lOne = [1, 5, 9, 2, 69, 72, 9, 75, 9]
lOne.sort()
print(lOne)
'''reverse the list'''
# reverse() will change the original lOne
lOne.reverse()
print(lOne)
'''apend new item at the end of list'''
# will change the original lOne
lOne.append("Fahim")
print(lOne)
'''insert new item in a specific index'''
# insert "suhan" on 9th index of lOne the prev item of 9th index will go to 10th index
lOne.insert(9, "suhan")
print(lOne)
'''pop an item with index from a list'''
# pop the item on 1th index from lOne
lOne.pop(1)
print(lOne)
'''remove a item with value from a list'''
# will remove "Fahim" from lOne
lOne.remove("Fahim")
print(lOne)

# count number of a item in a list
print(lOne.count("suhan"))

# know the index number of a item
print(lOne.index("suhan"))