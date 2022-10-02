# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# print normally
print("normally : ", a)

# printing original array
print("The new created array is : ", end=" ")
for i in range(3):
    print(a[i], end="")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print("Array after insertion : ", end=" ")
for i in a:
    print(i, end=" ")
print()

# using pop() to remove element at 3rd position/index
print("The popped element is : ", end="")
print(a.pop(3))

# printing array after popping
print("The array after popping is : ", end="")
for i in a:
    print(i, end=" ")

print("\r")



"""" Example 02 """


# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("The new created array is : ", end=" ")
for i in b:
    print(i, end=" ")
print()

# adding an element using append()
b.append(4.4)

print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()

# using remove() to remove 1st occurrence of 1
b.remove(2.5)

# printing array after removing
print("The array after removing is : ", end="")
for i in b:
    print(i, end=" ")