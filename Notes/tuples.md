### Tuple
* Tuples are used to store multiple items in a single variable.
* Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
* A tuple is a collection which is ordered and unchangeable.
* Tuples are written with round brackets.
```bash
thistuple = ("apple", "banana", "cherry")
print(thistuple) 
```
### Tuple Items
* Tuple items are 
  * **ordered** : When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
  * **unchangeable** : Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
  * **allow duplicate** Since tuples are indexed, they can have items with the same value.
* Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

####  Tuple length
```bash
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) 
```

#### Create Tuple With One Item
* To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
```bash
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 
```

#### Access tuples
```bash
thistuple = ("apple", "banana", "cherry")
# Ex 01
print(thistuple[1])

# Ex 02 Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
print(thistuple[-1])
```

* Range of indexes
```bash
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Ex 01
print(thistuple[2:5])

# Ex 02
print(thistuple[:4])
 
# Ex 03
print(thistuple[2:]) 

# Ex 04
print(thistuple[-4:-1])

```

### Check if item exits
```bash
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
```

### Change Tuple Values
* Once a tuple is created, you cannot change its values. Tuples are **unchangeable**, or **immutable** as it also is called.
* But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
```bash
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 
```
* But you **can add** a tuple to in another tuple
```bash
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) 
```

### Unpacking a tuple
```bash
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```
* **Note:** The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

### Loop tuple
```bash
# For loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
# While loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```

### Join tuple
```bash
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

### Multiply tuple
```bash
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```

### Tuples methods
* Python has two built-in methods that you can use on tuples.
  * count()	Returns the number of times a specified value occurs in a tuple
  * index()	Searches the tuple for a specified value and returns the position of where it was found

### Important resources
* [Python Tuples - very important](https://www.w3schools.com/python/python_tuples.asp)