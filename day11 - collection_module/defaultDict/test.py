# Python program to demonstrate
# defaultdict


from collections import defaultdict

"""Ex 01"""

# Defining the dict value type
d = defaultdict(int)
# these are keys the number of time a key is in there is the value..
L = [1, 2, 3, 4, 2, 4, 1, 2]
ll = ["Fahim","Suhan","Fahim"]

# Iterate through the list
# for keeping the count
for i in ll:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)


"""EX 02"""
# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)