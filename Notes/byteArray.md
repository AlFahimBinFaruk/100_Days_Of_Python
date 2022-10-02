### Byte Array in Python
* bytearray() method returns a bytearray object which is an array of given bytes. It gives a mutable sequence of integers in the range 0 <= x < 256.
* Returns: Returns an array of bytes of the given size.
* source parameter can be used to initialize the array in few different ways. Let’s discuss each one by one with help of examples.
* The main use case of byte array is 
  * converting an **object** into **byte object**.
  * creating an empty byte of specific size.

### Code #1: 
* If a string, must provided encoding and errors parameters, bytearray() converts the string to bytes using str.encode()
```bash
str = "Geeksforgeeks"
  
# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
  
print(array1)
print(array2) 
```

### Code #2: 
* If an integer, creates an array of that size and initialized with null bytes.
```bash
# size of array
size = 3
  
# will create an array of given size 
# and initialize with null bytes
array1 = bytearray(size)
  
print(array1) 
```

### Code #3: 
* If an Object, read-only buffer will be used to initialize the bytes array.
```bash
# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")
  
# iterating the value
for value in arr1:
    print(value)
      
# Create a bytearray object
arr2 = bytearray(b"aaaacccc")
  
# count bytes from the buffer
print("Count of c is:", arr2.count(b"c")) 
```

### Code #4: 
* If an Iterable(range 0<= x < 256), used as the initial contents of an array.
```bash
# simple list of integers
# String ,Float are not allowed in this case
list = [5, 2, 3, True]

# iterable as source
array = bytearray(list)

print(array)
print("Count of bytes:", len(array)) 
```

### Code #5: 
* If No source, an array of size 0 is created.
```bash
# array of size o will be created
  
# iterable as source
array = bytearray()
  
print(array) 
```

### Important resources
* [Byte Array in Python](https://www.geeksforgeeks.org/python-bytearray-function/)