### Set
* Sets are used to store multiple items in a single variable.
* Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
* A set is a collection which is **unordered**, **unchangeable**, and **unindexed**.
* Sets cannot have two items with the same value.
* Syntax:
```bash
# Ex 01
thisset = {"abc", 34, True, 40, "male"}
print(thisset)

# Ex 02
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
 
```

### Access Items
* You cannot access items in a set by referring to an index or a key.
* But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
```bash
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
```
* Check if an item is present in the set
```bash
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) 
```

### Add Items
* Once a set is created, you cannot change its items, but you can add new items:
```bash
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) 
```

### Add Sets
* To add items from another set into the current set, use the update() method.
```bash
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 
```

### Add Any Iterable
* The object in the update() method does not have to be a set, it can be any iterable object (**tuples**, **lists**, **dictionaries** etc.).
```bash
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 
```

### Remove Item
* To remove an item in a set, use the **remove()**, or the **discard()** method.
```bash
# Ex 01 : remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 
# Note: If the item to remove does not exist, remove() will raise an error.

# Ex 02 : discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.
```

* You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
The return value of the pop() method is the removed item.
```bash
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) 
```

* The **clear()** method empties the set(only an empty set will remain):
```bash
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 
```

* The **del** keyword will delete the set completely:
```bash
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) 
```

### Loop set
```bash
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

### Join two set
* There are several ways to join two or more sets in Python.
* You can use the **union()** and ,**intersection()** method that returns a new set containing all items from both sets, or the **update()**, **intersection_update()** method that inserts all the items from one set into another:
* union()
```bash
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 
```
* intersecion()
```bash
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z) 
```
* update()
```bash
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 
```
* intersection_update()
```bash
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x) 
```

* symmetric_difference_update() : **Keep All, But NOT the Duplicates**.The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
```bash
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x) 
```

* The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
```bash
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z) 
```

### set methods
* [All set methods](https://www.w3schools.com/python/python_sets_methods.asp)

### Resources
* [Python set](https://www.w3schools.com/python/python_sets.asp)